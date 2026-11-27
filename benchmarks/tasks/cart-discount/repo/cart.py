class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price_cents, qty=1):
        if price_cents < 0 or qty < 1:
            raise ValueError("invalid item")
        self.items.append((name, price_cents, qty))

    def total(self):
        return sum(p * q for _, p, q in self.items)
