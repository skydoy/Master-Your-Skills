# security reference: checklists by area

Read only the areas the change touches.

## Sinks and their safe APIs

| Value ends up in | Safe way |
|---|---|
| SQL or NoSQL query | Parameters or the ORM's query builder; never string building. Allowlist column names for dynamic sorting. |
| Shell command | Avoid the shell; pass an argument array to the process API. No interpolation. |
| HTML | Framework auto-escaping. Raw HTML only after an allowlist sanitizer. No `innerHTML` or `dangerouslySetInnerHTML` with user data. |
| URL in `href` or redirect | Allow only `http` and `https`; redirects only to known paths or hosts (open redirect). |
| File path | Resolve the full path, follow symlinks, check it is inside an allowed root. Delete, move and overwrite also need proof the target belongs to this job. |
| Server-side fetch | Allowlist scheme and host; resolve DNS and reject private, loopback and link-local addresses (including `169.254.169.254` and IPv6 forms); no redirects, or re-check after each. |
| `eval`, template engine, deserializer | Never with untrusted data. Use JSON, not language-native object formats. |
| Logs | No passwords, tokens, full card numbers or raw personal data; escape newlines to stop forged entries. |

## Authentication and sessions

- Passwords hashed with argon2, scrypt or bcrypt (cost 12+).
- Session cookies `HttpOnly`, `Secure`, `SameSite=Lax` or `Strict`, with an expiry. Auth tokens are not kept in `localStorage`.
- New session id after login and privilege change; sessions end on logout and password change.
- Reset and magic-link tokens: random, single use, expire within an hour, stored hashed.
- Login, reset and signup rate-limited (about 10 tries per 15 minutes per account and per IP), using a shared store when more than one instance runs.
- One response for unknown user and wrong password.
- JWTs: verify signature, algorithm, expiry, issuer and audience; never accept `none`.

## Authorization

- Every handler checks the caller may act on this specific record, not only that they are logged in. Load records scoped to the user or tenant (`WHERE owner_id = ?`).
- Admin routes check the role on the server.
- Mass assignment blocked: copy only allowed fields from the request body.
- API keys and service accounts have the least scope needed.

## Input and uploads

- Validate at the edge with a schema; reject unknown fields; cap string and array lengths and body size.
- Uploads: allowlist types, check the file's content not just its extension, cap size, store outside the web root with a generated name, serve with `Content-Disposition` and a safe content type.
- Webhooks: verify the signature over the raw body, reject old timestamps, handle repeats without side effects.

## Headers, CORS, errors

- Content-Security-Policy starting at `default-src 'self'`; HSTS; `X-Content-Type-Options: nosniff`; `frame-ancestors` or `X-Frame-Options` against framing.
- CORS: explicit origin list from config; never `*` together with credentials; do not reflect the request origin.
- Client errors are generic with a request id; stack traces stay in server logs.
- State-changing requests are not GETs; cookie-auth forms are protected by SameSite plus a CSRF token where needed.

## Secrets

- Read from environment or a secret manager; commit only `.env.example`; gitignore `.env*`, keys and certificates.
- Before commit: `git diff --cached` scan for keys, tokens and passwords (a secret scanner if the repo has one).
- Leaked: rotate, purge history, check access logs.

## Dependencies

- Use the project's package manager and committed lockfile; install with the frozen or immutable flag in CI.
- Run the manager's audit; triage high and critical by whether the vulnerable code is reachable in production. Do not run forced auto-fix; upgrade and test one at a time. Write down every deferral with a reason and date.
- Before adding a package: maintained, widely used, spelled right (typosquats), install scripts? Prefer the standard library for a few lines.

## Personal data

- Collect only what a feature needs; mark personal and sensitive fields.
- Each store of personal data has a retention period and a working delete path, including caches, search indexes, analytics and backups.
- Export and delete requests can find all of one user's data.
- Sending personal data to a vendor (analytics, email, LLM) needs consent or a legal basis and a data-processing agreement.

## LLM features

- Model output is untrusted input: validate against a schema before using it, and never pass it to a shell, SQL, `eval` or raw HTML.
- Text the model reads (user messages, web pages, documents) can carry instructions. Enforce permissions in code, not in the prompt.
- Keep secrets and other users' data out of the prompt. Scope tools to the user's rights; confirm destructive tool calls.
- Cap tokens, request rate and agent loop depth per user.
