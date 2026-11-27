# performance reference: usual bottlenecks and their fixes

Read only the section that matches the bottleneck you measured.

## Page load (LCP, first load)

- **Slow server response (TTFB over ~800ms).** Profile the server first. In the waterfall, long DNS or connection time to a third-party origin means `preconnect`; long "waiting" means the backend.
- **Large JavaScript.** Check what ships with a bundle analyzer. Split by route, lazy-load heavy rare features (editors, charts, maps), drop or replace large libraries. Rough budget: under 200KB gzipped for the first route.
- **Render-blocking resources.** Scripts in `head` get `defer`; non-critical CSS loads later; third-party widgets load after the page or behind a click-to-load facade.
- **The LCP element is an image.** Right size via `srcset` and `sizes`, AVIF or WebP, `fetchpriority="high"`, never `loading="lazy"` on it. Images below the fold get `loading="lazy"`.
- **Fonts.** WOFF2, self-hosted, two families at most, preload only the one used above the fold, `font-display: swap`.
- **Caching.** Hashed static files get a long `max-age`; HTML does not get `no-store` unless it must (it blocks the back/forward cache).

## Layout shift (CLS)

- Every image, video and iframe has `width` and `height` or an `aspect-ratio`.
- Space is reserved for ads, banners and late content.
- Fallback font metrics adjusted (`size-adjust`) when a web font swap moves text.
- Nothing is inserted above existing content after load, except in response to a user action.

## Slow interactions (INP)

- Find long tasks in the trace. Split work over 50ms into chunks and yield between them (`scheduler.yield()` where available, else `setTimeout`).
- Move non-urgent work (analytics, logging) out of the event handler.
- Lists with hundreds of rows: virtualize.
- React: stop creating new objects and functions in render for props of expensive children; memoize only components the profiler shows re-rendering at cost. Keep fast-changing state low in the tree.
- Avoid reading layout (`offsetHeight`, `getBoundingClientRect`) right after writing styles in a loop.
- Animate only `transform` and `opacity`.

## Backend endpoints

- **N+1 queries.** The query log shows one query per row. Load the relation in the same query (join, include, batch by ids).
- **Unbounded reads.** Every list endpoint has a limit and a stable sort; use keyset pagination for deep pages.
- **Missing or unused index.** Run `EXPLAIN ANALYZE` first. Seq scan on a big table: index the filter columns, equality first, then range or sort. Estimated rows far from actual: refresh statistics before adding anything. A function on the column (`lower(email)`) needs an expression index; a leading wildcard search needs trigram or full-text. Re-run the plan after; if it did not change, remove the index (it slows every write).
- **All endpoints slow at once.** Usually the connection pool: requests wait for a connection while the database is idle. Find what holds connections (long transactions, missing release) before raising the pool size. Keep instances times pool size under the database limit; use a pooler for serverless.
- **Repeated expensive work.** Cache only what is costly and read far more than written. Put every input that changes the result in the key. State how it goes stale (TTL or invalidation on write). Stop stampedes: one request recomputes while others wait or get the stale value. Never cache balances, permissions or stock at checkout.
- **Slow external calls.** Set timeouts, run independent calls in parallel, move work that the user need not wait for to a background job.

## Jobs, scripts, builds

- CPU profile first. Typical wins: work repeated inside a loop that could happen once, quadratic lookups that need a map or set, reading the same file or row many times, a regex that backtracks.
- Memory growth: take two heap snapshots apart in time and compare; look for caches or listeners that never shrink.
- Builds: cache dependency installs and build outputs between runs; run independent steps in parallel.

## Measurement tools

- Pages: browser DevTools Performance and Network panels, Lighthouse (lab), the `web-vitals` library or CrUX (field).
- Node: `--cpu-prof`, `clinic`, or `console.time` around suspect blocks.
- Python: `cProfile` with `snakeviz`, or `py-spy` on a running process.
- Databases: slow query log, `EXPLAIN ANALYZE`, `pg_stat_statements`.
- HTTP load: `autocannon`, `k6`, `hey`. Always report p50 and p95, not only the mean.
