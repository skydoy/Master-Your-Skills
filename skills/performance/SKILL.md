---
name: performance
description: Make something measurably faster: measure, find the bottleneck, fix it, re-measure, keep or revert. Use when a page, endpoint, query, build or script is slow, Core Web Vitals (LCP, INP, CLS) fail, latency regressed, or someone says "speed this up" or "why is this slow".
---

Spend effort only where a measurement shows time is lost, and keep only changes that measurably pay.

## Do this

1. **Name the metric and target.** One number the user feels: LCP, INP or CLS for pages (good is ≤2.5s, ≤200ms, ≤0.1), p95 latency for an endpoint, wall time for a job or build. No target given? Use those and say so.
2. **Make a repeatable measurement.** One command or script, fixed input, fixed conditions (warm or cold cache, same data size, throttled network for pages). Run it 5 times and record the median and the spread. This is the baseline.
3. **Find where the time goes** with a profiler, not by reading code:
   - Page load: network waterfall and Lighthouse trace. Big bundle, slow server response, render-blocking CSS/JS, unsized or huge images.
   - Slow interaction: performance trace, long tasks over 50ms, re-render counts.
   - Endpoint: per-request timing or tracing, the query log, `EXPLAIN ANALYZE` on the slowest query.
   - Job or script: a CPU profile or flame graph.
   Write: "X takes N of the M total because Y."
4. **Fix that one thing.** Usual suspects and fixes: the matching section of `reference.md`. Change one thing per measurement, or you cannot tell which change helped.
5. **Re-measure the same way** as the baseline, 5 runs. Keep the change only if the median moved by more than the spread and all tests pass. Within noise or worse: revert. Neutral code still costs upkeep.
6. **Log the attempt** in the PR or a `PERF.md` line: idea, baseline to result, kept or reverted, why. Reverted ideas leave no trace in git otherwise.
7. **Guard it** when the metric matters long term: a budget check in CI (bundle size, Lighthouse score, a timed test) or an alert on the field metric.

Small task (one obviously slow loop, one missing index): steps 2, 4 and 5 are enough, but still measure before and after.

## Stop and ask when

- The fix trades correctness or freshness for speed: caching data that must be live, dropping a validation, weakening consistency.
- The fix needs infrastructure (new cache server, CDN, bigger database, a new dependency).
- The target cannot be reached without a design change.

## Done when

- [ ] Baseline and result numbers exist, measured the same way, with run-to-run spread.
- [ ] The bottleneck is named in one sentence backed by a profile.
- [ ] Every kept change beats the noise; every neutral one was reverted.
- [ ] Tests pass with no test weakened to make the speedup work.
- [ ] Attempts are logged, including reverted ones.

## Traps

- Optimizing what looks slow in the code instead of what the profile shows.
- `useMemo` and `React.memo` everywhere; they cost too.
- Adding an index without reading the query plan before and after.
- A cache key missing an input (user, tenant, locale), which serves one user's data to another.
- Comparing a cold-cache baseline with a warm-cache result.
