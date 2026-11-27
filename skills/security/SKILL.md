---
name: security
description: Find and close security holes where untrusted data enters the code. Use when code handles user input, login, sessions, permissions, uploads, webhooks, server-side fetches, secrets, personal data, LLM output or new dependencies, or when asked "is this safe" or to harden it.
---

Check every place this change lets outside data in, prove each risk with a concrete attack, and fix it at that boundary.

## Do this

1. **List the entry points this change touches.** Request params, bodies, headers, cookies, uploads, webhooks, URLs the server fetches, queue messages, third-party responses, LLM output, paths and command arguments built from data. Trust follows who wrote the value, not how it arrived. Only these are in scope.
2. **Name what is at stake:** accounts, personal data, money, admin actions, other tenants' data, the server.
3. **For each entry point, ask five questions:**
   - *Who is calling?* Authentication present and checked on the server.
   - *May they touch this object?* Ownership or role checked for the specific record, every time (the most common real hole).
   - *Where does the value end up?* SQL, shell, HTML, file path, URL fetch, `eval`, a template, a log. Use that sink's safe API (see `reference.md`).
   - *How much can they send?* Size, rate and count limits; timeouts.
   - *What leaks back?* Response fields, error details, timing, logs.
4. **Write each finding as an attack:** "A user sends X to Y and gets Z." If you cannot phrase it that way, drop it. Rank by impact and ease.
5. **Fix at the boundary.** Validate with a schema (allowed shape, types, lengths, enums) and use only the parsed value after that. Prefer the framework's built-in protection. Add one test per fixed hole that sends the attack and expects refusal.
6. **Check the cross-cutting areas** the change touches (sessions, headers, CORS, dependencies, personal data) with `reference.md`.
7. **Search the diff for secrets** before any commit. A secret that reached a remote is burned: rotate it first, then clean history.

Small change with no new entry point: step 7, plus step 3 on the touched code.

## Stop and ask when

- Changing authentication, session handling, permissions or CORS.
- Storing a new kind of sensitive data, or sending personal data to a new third party.
- A dependency audit fix would force a major version jump.
- You find a live secret or a hole exploitable in production: report it first.

## Done when

- [ ] Every entry point the change touches has a server-side authentication and object-level authorization check.
- [ ] Every value reaching a dangerous sink goes through the safe API for that sink.
- [ ] Each fixed hole has a test that performs the attack and gets refused.
- [ ] No secrets in the diff or history; errors show no internals.
- [ ] New or updated dependencies were audited and reviewed.

## Traps

- Checking that the user is logged in but not that the record is theirs.
- Validation only in the browser.
- An allowlist on the URL string but not on the resolved IP, so the server can still reach internal addresses.
- Treating LLM output or another service's response as trusted.
- An in-memory rate limiter on a multi-instance deploy.
