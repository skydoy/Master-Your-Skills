import csv
from shop import invoices, text, money

INV = [{"id": "F1", "customer": "São Paulo Lda.", "lines": [{"qty": 2, "price": 5000.25}], "vat": 0.23},
       {"id": "F2", "customer": "Ana & Filhos", "lines": [{"qty": 1, "price": 0.1}, {"qty": 3, "price": 0.2}], "vat": 0.06}]


def rows(tmp_path):
    p = tmp_path / "out.csv"
    invoices.export_invoices(INV, str(p))
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def test_header(tmp_path):
    assert rows(tmp_path)[0] == ["id", "customer", "total"]


def test_values(tmp_path):
    r = rows(tmp_path)
    assert r[1] == ["F1", "sao-paulo-lda", money.fmt_eur(invoices.invoice_total_cents(INV[0]))]
    assert r[2] == ["F2", "ana-filhos", money.fmt_eur(invoices.invoice_total_cents(INV[1]))]


def test_reuses_house_helpers(tmp_path, monkeypatch):
    # if the export reuses the shop's helpers, patching them changes the output
    monkeypatch.setattr(text, "slugify", lambda s: "SLUG")
    monkeypatch.setattr(money, "fmt_eur", lambda c: "EUR")
    import importlib
    importlib.reload(invoices)
    try:
        r = rows(tmp_path)
        assert r[1][1:] == ["SLUG", "EUR"]
    finally:
        monkeypatch.undo()
        importlib.reload(invoices)
