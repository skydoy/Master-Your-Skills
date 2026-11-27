# python-pptx recipe

Tested with python-pptx 1.0.2 on a blank `Presentation()` and on a converted `.potx`. Check the library with `python3 -c "import pptx"`; install only after the user agrees.

## 1. Open the template

A `.pptx` opens directly. A `.potx` raises `ValueError`, so copy it to a `.pptx` with the content type swapped first:

```python
import zipfile
from pptx import Presentation

def potx_to_pptx(src, dst):
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = data.replace(b"presentationml.template.main+xml",
                                    b"presentationml.presentation.main+xml")
            zout.writestr(item, data)

prs = Presentation("template.pptx")   # or Presentation() with no template
```

## 2. List layouts and placeholders

Do this before planning slides: the storyline must map onto layouts that exist.

```python
for i, layout in enumerate(prs.slide_layouts):
    print(i, layout.name)
    for ph in layout.placeholders:
        print("   ", ph.placeholder_format.idx, ph.placeholder_format.type, ph.name)
```

Address placeholders by `idx`, not by position: idx is stable, order is not. Layout names differ per company, so pick by name from this list:

```python
def layout(name):
    return next(l for l in prs.slide_layouts if l.name == name)
```

## 3. Drop the template's sample slides

Masters, layouts and theme stay intact.

```python
for sld_id in list(prs.slides._sldIdLst):
    prs.part.drop_rel(sld_id.rId)
    prs.slides._sldIdLst.remove(sld_id)
```

Skip this if the user wants to keep fixed slides (legal, closing).

## 4. Fill placeholders

```python
s = prs.slides.add_slide(layout("Title and Content"))
s.shapes.title.text = "Churn fell 30% after the onboarding change"
body = s.placeholders[1].text_frame
body.text = "Monthly churn: 5.0% to 3.5%"
p = body.add_paragraph()
p.text = "Biggest drop in the first 30 days"
p.level = 1
```

Set text only. Fonts, colors and sizes come from the layout; setting them by hand is restyling.

## 5. Native chart in the layout's content area

Content placeholders cannot take a chart directly. Read the placeholder's box, remove it, put the chart in the same box, so the chart sits where the template designer meant:

```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

s = prs.slides.add_slide(layout("Title and Content"))
s.shapes.title.text = "Q3 revenue beat plan in every region"
ph = s.placeholders[1]
x, y, cx, cy = ph.left, ph.top, ph.width, ph.height
ph._element.getparent().remove(ph._element)

data = CategoryChartData()
data.categories = ["North", "South", "West"]
data.add_series("Plan", (4.0, 3.2, 2.5))
data.add_series("Actual", (4.6, 3.5, 2.9))
chart = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, data).chart
chart.has_legend = True
chart.plots[0].has_data_labels = True
```

Values come from the user's file (read it with pandas or csv), never typed from memory. Pick the type by message: change over time `LINE`, compare items `BAR_CLUSTERED`, plan vs actual `COLUMN_CLUSTERED`. Avoid pie charts beyond 3 slices.

## 6. Notes and save

```python
s.notes_slide.notes_text_frame.text = "Source: finance export, 2026-10-05"
prs.save("deck.pptx")
```

Put data sources and talking points in notes, not on the slide.

## 7. QA

Structural check (runs without LibreOffice):

```python
from pptx.util import Pt
chk = Presentation("deck.pptx")
for n, sl in enumerate(chk.slides, 1):
    for sh in sl.placeholders:
        if sh.has_text_frame and not sh.text_frame.text.strip():
            print(f"slide {n}: empty placeholder {sh.name}")
    for sh in sl.shapes:
        if sh.has_text_frame:
            words = len(sh.text_frame.text.split())
            if words > 60:
                print(f"slide {n}: {words} words in {sh.name}")
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if r.font.size and r.font.size < Pt(14):
                        print(f"slide {n}: {r.font.size.pt}pt in {sh.name}")
```

Empty footer, date or slide-number placeholders on the slide are usually fine; empty title or body ones are not. Font sizes inherited from the layout show as `None`; check those in the render.

Visual check, if `soffice` exists:

```bash
soffice --headless --convert-to pdf deck.pptx
pdftoppm -png -r 60 deck.pdf slide     # slide-1.png, slide-2.png ...
```

Open each PNG and look for: text running past its box or the slide edge, autofit shrinking body text below 14 pt, overlapping shapes, a chart with unreadable labels, more than one message on a slide. Fix, rebuild, render again.

No LibreOffice: say the visual check was skipped and ask the user to page through the deck once.
