import pandas as pd
from app.utils.pricing import calculate_price

def pricing(products):
    rows = []
    for p in products:
        price = calculate_price(p["cost_price"], p["shipping_cost"])
        rows.append({"sku": p["supplier_sku"], "price": price, "stock": p["stock"]})
    return pd.DataFrame(rows)