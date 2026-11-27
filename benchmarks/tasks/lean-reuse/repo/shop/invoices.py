from .money import to_cents


def invoice_total_cents(invoice):
    """invoice = {"id": str, "customer": str, "lines": [{"qty": int, "price": float}], "vat": 0.23}"""
    net = sum(to_cents(l["price"]) * l["qty"] for l in invoice["lines"])
    return net + to_cents(net * invoice["vat"] / 100)
