# quality-bar reference

## Default numbers (use when the user has none)

| Rule | Default | Why |
|---|---|---|
| Coverage of changed lines | 80% or more | Forces a test, still allows a config line |
| Whole-project coverage | today's value, must not fall | Nothing to argue about |
| Mutation score (if used) | 60% or more to start | Normal for a suite never mutated |
| Dependency vulnerabilities | none at high or critical | Lower levels are mostly noise |
| Largest Contentful Paint | 2500 ms or less | Web "good" threshold |
| Layout shift (CLS) | 0.1 or less | Same source |
| Accessibility | zero critical or serious axe issues | Lower levels are often debatable |
| Exception lifetime | 90 days | Long enough to plan, short enough to remember |
| Ratchet tolerance | 0.5% | Absorbs noise from unrelated files |

Write the reason next to every number. A number without a reason gets deleted by the next person it blocks.

## One established tool per dimension

Prefer what the project already runs. Otherwise:

| Dimension | Tool and command | Fails on |
|---|---|---|
| Types | `tsc --noEmit`, `mypy .`, `go vet` | any error |
| Lint | existing config: `eslint .`, `biome check`, `ruff check` | any error |
| Changed-line coverage | runner's lcov output intersected with `git diff` (no second test run) | below the number |
| Secrets | `gitleaks dir . --redact` | any finding |
| Dependencies | `osv-scanner scan source -r .` or the package manager's audit | high or above |
| Code security | `semgrep scan --config p/default --json` | high or above |
| Page speed | `lighthouse $URL --output=json` | budget missed |
| Bundle size | `size-limit --json` | byte budget missed |
| Accessibility | `axe $URL --tags wcag2a,wcag2aa` | critical or serious |
| Layer rules | `depcruise src` | any violation |

Notes:
- Lighthouse and axe need a running URL; run them against a preview or a local server, or drop them.
- semgrep and axe can exit 0 even with findings. Parse their JSON and exit non-zero on the agreed severity.
- Scope slow tools to changed files (semgrep path list, mutation testing on touched files).
- Always redact secrets; report rule and file:line only.

Put commands in the project's own scripts (`check:fast`, `check:task`, `check:full`) so they run without an agent. `CONSTRAINTS.md` stays the source of truth; scripts mirror it.

## Diff guard patterns (step 7)

Diff against the merge base, plus untracked files:

```
base=$(git merge-base origin/main HEAD) || exit 2
git diff --unified=0 "$base" --
git ls-files --others --exclude-standard   # diff each with: git diff --no-index /dev/null <file>
```

Exit 0 clean, 1 violation, 2 could not run. Never let "could not run" count as clean.

Flag added lines (`+`) matching:
- Suppression: `@ts-ignore|@ts-nocheck|@ts-expect-error|eslint-disable|biome-ignore|# *noqa|# *type: *ignore|istanbul ignore|nosemgrep|gitleaks:allow|Stryker disable|#\[allow\(|//nolint`
- Skip: `\.(skip|only|todo)\b|\bx(it|describe)\(|@pytest\.mark\.(skip|xfail)|t\.Skip\(|@Disabled|#\[ignore\]`
- Stub: `not implemented|NotImplementedError|todo!\(|unimplemented!\(|catch *(\(\w*\))? *\{ *\}|except.*: *pass$`
- New exception row in `CONSTRAINTS.md`.

Flag removed lines (`-`):
- In a test file that still exists, matching `expect|assert|should|require\.`.
- A whole test file deleted.
- A rule row or bullet in `CONSTRAINTS.md` with no matching added line (removed rule).
- A rule whose number moved the loose way: a minimum went down or a maximum went up. If the direction is unclear, flag any change.

`.only` is included because it silently skips every other test.

Each hit needs a stated reason in the change or a dated exception row; otherwise fix the code.
