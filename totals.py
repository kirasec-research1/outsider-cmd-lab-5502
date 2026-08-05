def compute_total(items):
    t = 0
    for i in items:
        t += i["qty"] * i["price"]
    return t
