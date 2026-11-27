SALES = [
    {"region": "Norte", "amount": 1200.5},
    {"region": "Sul", "amount": 980.0},
    {"region": "Norte", "amount": 300.25},
    {"region": "Centro", "amount": 1500.0},
    {"region": "Sul", "amount": 20.0},
]


def totals_by_region(sales=SALES):
    out = {}
    for s in sales:
        out[s["region"]] = out.get(s["region"], 0) + s["amount"]
    return out
