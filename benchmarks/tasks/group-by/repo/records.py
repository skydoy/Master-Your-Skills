def total(records, field):
    return sum(r[field] for r in records)
