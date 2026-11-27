# ship reference

Read only the section a SKILL.md step points to. Mark what doesn't apply n/a.

## CI

Cheapest gates first, so most failures surface in seconds:

1. Install from the lockfile (`npm ci`, `--locked`).
2. Lint and format check.
3. Type check.
4. Unit tests.
5. Build the real artifact.
6. Integration tests against real services in containers.
7. End-to-end tests on critical flows only; keep traces on failure.
8. Dependency audit, high severity and up.
9. Size or performance budget, if any.

Setup rules:
- Run on every pull request and on pushes to the default branch.
- Protect the default branch: required checks, one approval, no force-push.
- Secrets live in the CI secret store, never in workflow files. CI never holds production credentials.
- Pass user-controlled values (branch names, inputs) via environment variables, never pasted into shell lines (injection).
- Keep it under ~10 minutes. If slower, in order: cache downloads, parallel jobs, path filters, shard tests, move slow suites to a schedule.
- A flaky test is a bug. Quarantine it with an owner and a date, then fix it; do not re-run until green.
- On failure: read the first real error, reproduce locally, fix the cause.

## Telemetry

Pick the signal by the question:
- "How often, how fast, overall?" → metric. Per endpoint and outside dependency: rate, errors, latency histogram. Per pool or queue: utilization, saturation, errors.
- "Where did the time go across services?" → trace. Auto-instrument first; hand spans only around meaningful work.
- "Why did this one case fail?" → structured log.

Logs:
- One JSON object per event, with a stable event name (`payment_failed`) and fields, not an interpolated sentence.
- Levels: `error` means someone may need to act; `warn` means handled but degraded; `info` for business events; `debug` off in production.
- Set a request ID at the edge and carry it through every call, message and log line. If several entry points (scheduler, webhook, manual run) share a log, stamp which one started the run.
- Never log secrets or full personal data. Allowlist fields; no whole request bodies.

Metrics:
- Labels from small fixed sets (route template, `5xx`, provider). User IDs, URLs and error text go in logs: each unique label value is a new series.
- Latency as a histogram; read p50, p95, p99.

Alerts:
- Page on what users feel (error rate, p99 latency, queue age), not on causes (CPU, one pod restart). Causes go on a dashboard.
- Two levels only: page now, or ticket this week.
- Each alert has a justified threshold and duration, and a runbook: what it means, first check, who to escalate to. Fire it once to prove it arrives.

Proof: break something in staging and find the cause from telemetry alone.

## Rollout

Compare each stage to the pre-launch baseline over enough real traffic (hours for a canary).

| Signal | Advance | Hold and look | Roll back |
|---|---|---|---|
| Error rate | within 10% of baseline | 10% to 2x | above 2x |
| p95 latency | within 20% | 20% to 50% | above 50% |
| New client error types | none | under 0.1% of sessions | over 0.1% |
| Key business metric | flat or up | down under 5% | down over 5% |

Roll back at once on data corruption, a security issue or a spike in user reports.

Error budget: over 20% left, normal; under 20%, small careful rollouts; spent, reliability fixes only.

Flags: owner, removal date, no nesting, CI tests both states, removed ~2 weeks after full rollout.

Rollback plan, before deploy: trigger values; steps (flag off, redeploy build X, down-migration Y); checks after; who is told.

First hour: health check up, no new error types, latency normal, main flow works by hand, logs arriving.

## Pre-launch sweep

First launch or large release only: run the `security`, `performance` and `accessibility` skills on the release diff, then confirm production env vars are set, migrations are ready, a health endpoint and error reporting exist, and the changelog and setup docs match what ships.

## Phased change of a shared shape

Example: rename column `name` to `full_name`.
1. Add `full_name`, nullable. Deploy.
2. Write both columns on every insert and update. Deploy.
3. Backfill in small throttled batches; build big indexes without locking writes.
4. Read from `full_name`, still write both. Deploy and wait.
5. Stop writing `name`. Deploy.
6. Drop `name` in its own later deploy.

Same order for API fields and events: add, dual-publish, move consumers, measure zero use, remove. If you own the old thing, migrating its users is your job: publish the replacement, reason, date if forced, and copy-paste steps.
