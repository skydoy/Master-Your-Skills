---
name: api-design
description: Design or change an interface other code depends on: REST or GraphQL endpoints, module contracts, component props, event payloads. Covers types, errors, validation, pagination, safe retries and versioning. Use for "design an API", "add an endpoint", "change this contract", "is this breaking".
---

Once someone calls your interface, every visible behavior becomes a promise: field names, error text, ordering, timing. Design so the right call is easy, the wrong call fails loudly, and growth never breaks a caller.

## Do this

1. **Write the contract before the code:** input type, output type, every error case, one line per operation on its behavior (partial update? idempotent?). Agree on it, then implement.
2. **Expose the minimum.** Every field is a promise. Return what callers need, not your database row. Keep input and output types separate so server fields (id, timestamps) are never inputs.
3. **One error shape everywhere.** For HTTP, a status that matches the cause (400 malformed, 401 not signed in, 403 forbidden, 404 missing, 409 conflict, 422 invalid, 500 our fault) and a body like `{ error: { code, message, details? } }`. `code` is stable for machines, `message` is for people. Never leak stack traces or SQL. Never mix throwing, returning null and returning error objects.
4. **Validate where data enters:** handlers, forms, environment config, and every third-party response (treat it as hostile). Inside the trusted core, rely on types.
5. **Name predictably:** plural nouns plus HTTP verbs (`POST /orders`, not `/createOrder`), one casing, booleans as `isX`/`hasX`. The codebase's existing conventions win over general rules.
6. **Paginate every list from day one**, with a capped page size; adding it later changes the response shape.
7. **Make retries safe for state changes.** Accept an idempotency key or document the call as unsafe to retry. With a key:
   - The client makes it once per intent and reuses it on retry, never per attempt.
   - Claim it with one atomic insert under a unique constraint; "check, then act" is a race.
   - Same key, different body: return an error, not the old response.
   - Decide what a mid-flight duplicate gets: 409, wait, or 202 with a status link.
   - Keep keys longer than the longest retry or replay path.
8. **Change by adding.** New fields are optional; never rename, remove or retype in place. For a real break, ship the new form beside the old, migrate callers, remove the old on an announced date.
9. **Contract-test** each success shape and each error code.

Internal function, two callers? Steps 1–3 and 8 suffice.

## Stop and ask when

- An existing caller you don't control would break.
- You would need two live versions; one is far cheaper to run.
- Auth, money or personal-data rules are unclear.

## Done when

- Inputs, outputs and error cases are typed and written down.
- One error shape and one naming style across the API.
- Lists paginate; state changes are idempotent or marked unsafe to retry.
- No existing field removed, renamed or retyped.
- Tests cover each success shape and error code.

## Traps

- Response shape that varies with conditions.
- An idempotency key accepted but not stored with its result: clients retry into double charges.
- "Nobody uses that quirk": someone does.
