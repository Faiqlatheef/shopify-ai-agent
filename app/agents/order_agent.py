def process_orders(orders, products):
    actions = []
    stock_map = {p["supplier_sku"]: p["stock"] for p in products}

    for _, o in orders.iterrows():
        sku = o["sku"]
        qty = o["quantity"]

        if stock_map.get(sku, 0) >= qty:
            action = "fulfill"
        else:
            action = "backorder"

        actions.append({
            "order_id": o["order_id"],
            "action": action,
            "email": f"Your order {action}"
        })
    return actions