---
name: spreadsheet-help
description: Explains and writes Excel or Google Sheets formulas, pivot tables and charts from what the user wants to get. Use for "excel formula", "fórmula excel", "PROCV", "tabela dinâmica", "pivot table", "gráfico", "sum if", "why does my formula fail".
---

Give a formula that works on the user's real layout, where to paste it, and a way to prove it.

## Mode

- **Direct**: the user gave columns, sample rows and the goal. Answer at once.
- **Guided**: otherwise ask one round, max 6 questions, each with a suggested answer: Excel or Google Sheets [Excel]; language of Excel [English]; column letters and headers [?]; 3-5 sample rows with the expected result [?]; where the result goes [cell F2]; any blanks, text-as-number or duplicates [no]. Max 2 rounds.

Reply in the user's language.

## Do this

1. Restate the goal in one line, with the exact ranges.
2. Give the formula in a code block, using the user's real columns. Prefer simple, robust functions: SUMIFS, COUNTIFS, XLOOKUP (or INDEX/MATCH if the version is old, and always in Google Sheets VLOOKUP/INDEX-MATCH if XLOOKUP is unavailable), IFERROR, TEXT, SUMPRODUCT. Avoid volatile or nested monsters; split into helper columns when clearer.
3. Say where to paste it ("cell F2, then drag down" or "double-click the fill handle") and whether it needs array entry.
4. Explain it in 2-4 lines, one argument per line.
5. Give a check: compute one row by hand, or compare with a total (SUM of results equals the original total), or filter and count.
6. For pivot tables: list the steps (Insert > PivotTable), what goes in Rows, Columns, Values, Filters, and the summary type. For charts: type, data range, axis labels, and why that type.
7. For an error (#N/A, #VALUE!, #REF!, #NAME?), name the likely cause from the formula and the data, and give the fixed formula.

## Portuguese Excel

If the user's Excel is in Portuguese (or says "PROCV", "SE", "SOMA.SE.S"), use Portuguese function names and `;` as the separator, and decimals with a comma. Common pairs (Portugal / Brazil where they differ): IF = SE, VLOOKUP = PROCV, XLOOKUP = PROCX, SUMIFS = SOMA.SE.S / SOMASES, COUNTIFS = CONTAR.SE.S / CONT.SES, IFERROR = SE.ERRO / SEERRO, AND = E, OR = OU, TEXT = TEXTO, INDEX/MATCH = ÍNDICE/CORRESP. Ask which country if unsure. In Google Sheets, function names stay English even if the interface is Portuguese; the separator depends on the sheet locale, so give `,` and note `;` if it errors.

## Stop and ask when

The data is ambiguous (merged cells, dates stored as text) and two layouts would need different formulas.

## Done when

- The formula refers to the user's real columns.
- Paste location and a check are given.
- Separators and names match the user's language.

## Traps

- Whole-column ranges in heavy sheets.
- Forgetting absolute references ($A$1) when dragging.
- Numbers stored as text: check with ISNUMBER.

End with "Check before using": test on 3 rows with known answers, confirm locale separators, and keep a copy of the sheet before filling down.
