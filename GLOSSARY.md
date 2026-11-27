# Glossary

Every skill, what it is for, and what it measurably changes. Call a skill by name (`/master-your-skills:<name>`) or just describe the task; `start` routes vague requests.

## Measured gains

Same task and model, run with and without the skill; hidden tests decide "correct". Skills not in this table have not been benchmarked yet.

<!-- gains:start -->
| Skill | Task | Runs | Correct (without → with) | Wrote a test | Output tokens |
|---|---|---|---|---|---|
| `check-code` | review-cross | 4+4 | 100% → 100% | 0% → 0% | +35% |
| `check-code` | review-diff | 3+3 | 100% → 100% | 0% → 0% | +33% |
| `debug` | fix-duration | 3+3 | 100% → 100% | 0% → 100% | +90% |
| `email` | email-reply | 4+4 | 75% → 83% | 0% → 0% | +21% |
| `lean` | group-by | 3+3 | 100% → 100% | 0% → 0% | +20% |
| `lean` | json-flag | 3+3 | 100% → 100% | 0% → 0% | +13% |
| `lean` | lean-reuse | 4+4 | 100% → 100% | 0% → 0% | -10% |
| `start` | start-export | 4+4 | 25% → 100% | 0% → 0% | +119% |
| `tdd` | cart-discount | 3+3 | 100% → 100% | 0% → 100% | +290% |
<!-- gains:end -->

![Benchmark](docs/img/benchmark.png)

## All skills

### Start

| Skill | Use it for |
|---|---|
| `start` | Entry point. Picks the right skills for a request and turns a vague ask into a confirmed brief with one round of questions, each with a suggested answer. Use at the start of work, or when the user says "I want to build", "help me with", "where do I start", "which skill". |

### Always on

| Skill | Use it for |
|---|---|
| `lean` | Always-on base for coding work. Solve the whole task with the least new code, touch only what the task needs, and end by saying what was skipped. Use on any write, fix or refactor, and when the user says "keep it simple", "yagni", "too much code", "over-engineered". |

### Define

| Skill | Use it for |
|---|---|
| `spec` | Write a short spec before building new or unclear work, and get it approved before any code. Use for a new feature, project or significant change, a vague requirement, or when the user says "write a spec", "PRD", "requirements", "scope this", "what exactly are we building". |
| `plan-work` | Break an approved spec or clear request into ordered, vertical-slice tasks, each with acceptance checks, a verify command and its blockers. Use when the user says "plan this", "break it down", "make tickets", "task list", or when work is too big to start in one go. |
| `prototype` | Build a throwaway prototype that answers one design question, then keep the answer and bin the code. Use when someone asks "will this state model hold up?", "what should this page look like?", wants to try a few layouts, or wants to click through logic before building it for real. |

### Design

| Skill | Use it for |
|---|---|
| `api-design` | Design or change an interface other code depends on: REST or GraphQL endpoints, module contracts, component props, event payloads. Covers types, errors, validation, pagination, safe retries and versioning. Use for "design an API", "add an endpoint", "change this contract", "is this breaking". |
| `design-code` | Shape or reshape code structure so each module hides a lot behind a small interface. Use for "improve the architecture", "this code is hard to change", "where should this boundary go", "make it testable", "clean up / simplify this module", or before adding a new layer or abstraction. |

### Build

| Skill | Use it for |
|---|---|
| `frontend-ui` | Build or change user-facing UI that looks deliberate, not AI-generated. Use when making a page, screen, component, form, dashboard or landing page, when picking colors, fonts or spacing, or when someone says the UI "looks generic" or "looks like AI". |
| `build` | Implement a plan or ticket in small working slices, each one tested, verified and committed before the next. Use when the user says "implement this", "build the plan", "do task 3", "work through the tickets", or a change will touch more than one file. |
| `tdd` | Write the failing test first, then the code, one behavior at a time, with tests that catch real bugs. Use when the user says "TDD", "test first", "red-green", "add tests", or when you implement logic, fix a bug, or change behavior. |
| `parallel` | Split work across parallel subagents and merge the results safely. Use when the user says "run these in parallel", "fan out", "use subagents", "spin up a team", or when a task has several independent parts (separate bugs, modules, files, questions) that could run at the same time. |
| `context-diet` | Load the least context that gets the task right. Use when starting a session or new task, when answers drift or invent APIs, before writing code against a versioned library, when the conversation is long or "context is full", or to write a handoff note so a fresh session can continue. |

### Verify

| Skill | Use it for |
|---|---|
| `debug` | Find the root cause of a bug with a fast repro loop, fix it once, and lock it with a test. Use when something is broken, throws, fails, is flaky or slow, when a test or build goes red, or the user says "debug", "why does this fail", "it worked yesterday". |
| `check-code` | Review a change for bugs, security, load, missing tests, speed and needless code, with ranked findings in plain words. Use when the user says "check this", "review my PR", "review the last commit", "is this ready to merge", "is this over-engineered", or before merging any change. |
| `browser-test` | Check a web change in a real browser: console, network, DOM, accessibility tree, screenshots. Use when a UI change needs proof it works, a page renders or behaves wrong, or when asked to "open it in the browser", "take a screenshot", "check the console" or "write a Playwright test". |
| `accessibility` | Audit an existing page or component against WCAG 2.2 AA and fix what fails. Use for an accessibility or a11y audit, running axe or pa11y, triaging a11y violations, or when "screen reader can't read this", "keyboard doesn't work" or "contrast is too low" comes up. |
| `performance` | Make something measurably faster: measure, find the bottleneck, fix it, re-measure, keep or revert. Use when a page, endpoint, query, build or script is slow, Core Web Vitals (LCP, INP, CLS) fail, latency regressed, or someone says "speed this up" or "why is this slow". |
| `security` | Find and close security holes where untrusted data enters the code. Use when code handles user input, login, sessions, permissions, uploads, webhooks, server-side fetches, secrets, personal data, LLM output or new dependencies, or when asked "is this safe" or to harden it. |
| `audit` | Read-only health check of a repo or folder: defects, security gaps, scaling limits, untested risky logic, slow spots, dead weight, and a ledger of `shortcut:` debt markers. Use for "audit this repo", "what can I delete", "list the shortcuts", "tech debt". |
| `quality-bar` | Write the project's quality bar once in CONSTRAINTS.md with real commands and numbers, then refuse any change that quietly lowers it (skipped tests, ts-ignore, eslint-disable, removed asserts, lowered thresholds, stubs). Use for "set our standards", "add quality gates", "stop the agent cheating to green". |

### Ship

| Skill | Use it for |
|---|---|
| `git` | Turn work into clean git history and reviewable pull requests. Use when committing, writing a commit message, splitting a messy working tree into commits, naming or cleaning up branches, opening or describing a PR, tagging a release, picking a version bump or writing a changelog entry. |
| `ship` | Get a change to production safely and keep it healthy. Use when deploying or launching, asking "is this ready to ship?", setting up CI gates, planning a staged rollout or rollback, adding logs/metrics/alerts, or removing an old API, feature or database column. |
| `docs` | Write down decisions and domain terms so they stay true. Use when recording an architecture decision (ADR), defining or settling project vocabulary (GLOSSARY.md), updating a README or API docs after a change, or checking whether a doc is stale or "out of date" with the code. |

Office skills work in two modes: **Direct** (paste everything, get the result) or **Guided** (one round of questions, each with a suggested answer). They never invent facts: anything missing shows as `[VALUE]`.

### Office: write and present

| Skill | Use it for |
|---|---|
| `speech` | Writes speeches and talks sized to the minute, made for the ear rather than the page. Use when the user says "write a speech", "toast", "keynote", "talk", "remarks for", "wedding speech", "opening words", "I have to speak at". |
| `deck` | Builds corporate PowerPoint decks on the company template, storyline first, with native charts from real data and a rendered QA pass. Use when the user says "make a deck", "PowerPoint", "slides for", "presentation for the board", "build on our template", or gives a .pptx/.potx. |
| `email` | Writes new emails and replies that sound like a person wrote them. Use when the user says "write an email", "draft a reply", "answer this email", "reply to", "how do I respond", "email to my boss/client", or pastes an email and asks what to say. |

### Office: leaders

| Skill | Use it for |
|---|---|
| `exec-brief` | Turns long reports, email threads or data into a one-page executive brief with decision, 3 key facts, risks, numbers, recommendation and cost of inaction. Use for "executive summary", "one-pager", "brief for the CEO", "resumo executivo", "resumir este relatório". |
| `decision` | Compares 2-5 options against explicit weighted criteria (cost, risk, time, reversibility), shows the trade-off table, recommends one and names what would change it. Use for "compare options", "which should we choose", "decision memo", "decidir entre", "comparar opções". |
| `board-pack` | Assembles a board or committee meeting pack from loose inputs: agenda, a paper per item with decision requested, KPIs vs target, risks, appendices; flags what is missing. Use for "board pack", "committee papers", "pauta da reunião", "pacote para o conselho". |
| `okr` | Converts strategy text into 3-5 objectives, each with 2-4 measurable key results, owners, baselines and targets; rejects activities disguised as results. Use for "write OKRs", "turn strategy into goals", "metas trimestrais", "objetivos e resultados-chave". |
| `crisis-comms` | Fast, facts-only drafts for an incident: internal note, customer or public statement, press holding line and FAQ, with what we know, don't know and next update time. Use for "incident statement", "outage message", "press line", "comunicado de crise", "nota de imprensa". |

### Office: managers

| Skill | Use it for |
|---|---|
| `meeting` | Prepares a meeting agenda (goal and time box per item) or writes minutes from notes or a transcript (decisions, owners, deadlines, open questions). Use for "meeting agenda", "prepare a meeting", "meeting minutes", "ata da reunião", "pauta", "resumir reunião". |
| `weekly-status` | Turns loose notes into a weekly project status report with traffic light, done, next, blockers and metrics vs plan. Use for "weekly status", "status report", "project update", "relatório semanal", "status do projeto", "RAG status". |
| `feedback-review` | Writes fair, specific performance reviews and feedback using situation-behaviour-impact, strengths, growth areas and agreed goals, and flags biased or vague wording. Use for "performance review", "give feedback", "avaliação de desempenho", "feedback para", "review wording". |
| `project-plan` | Builds a project plan table with tasks, owners, dates, dependencies, risks, critical path and milestones, as Markdown or CSV for Excel; asks for deadline and team capacity. Use for "project plan", "timeline", "cronograma", "plano de projeto", "work breakdown". |
| `delegate` | Turns an idea into one clear, ready-to-send request for the team with what, why, deadline, success measure, constraints and who to ask. Use for "delegate this", "write a request for my team", "delegar tarefa", "pedido para a equipe", "assign this task". |

### Office: everyday work

| Skill | Use it for |
|---|---|
| `sop` | Writes or improves a step-by-step procedure (SOP) from a rough or spoken explanation. Use for "write a procedure", "SOP", "how-to for the team", "document this process", "procedimento", "passo a passo", "instrução de trabalho". |
| `summarize-doc` | Summarises a contract, manual or long email for a specific task: what it means for you, deadlines, obligations, numbers, risks, with page references. Use for "summarise this", "what do I need to do", "resumir contrato", "resumo do documento", "prazos e obrigações". |
| `clear-request` | Turns a problem into a clear request to a boss, IT support or a supplier: what happened, impact, what was tried, what is needed, by when. Use for "write to IT", "ask my manager for", "report a problem", "pedido ao fornecedor", "escrever ao suporte", "reclamação". |
| `spreadsheet-help` | Explains and writes Excel or Google Sheets formulas, pivot tables and charts from what the user wants to get. Use for "excel formula", "fórmula excel", "PROCV", "tabela dinâmica", "pivot table", "gráfico", "sum if", "why does my formula fail". |
| `plan-my-day` | Turns a task list into a realistic day plan by priority, deadlines, effort and energy, with time blocks, buffers, and what to drop or delegate. Use for "plan my day", "I have too much to do", "organise my tasks", "planear o dia", "organizar tarefas", "prioridades". |
