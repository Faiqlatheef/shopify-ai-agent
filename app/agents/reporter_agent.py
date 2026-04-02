def generate_report(products, orders, issues):
    return f"""
# Daily Report

Products: {len(products)}
Orders: {len(orders)}
Issues Found: {len(issues)}
"""