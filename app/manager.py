from app.utils.io import read_csv, write_json, write_csv

from app.agents.product_agent import select_products
from app.agents.listing_agent import generate_listings
from app.agents.pricing_agent import pricing
from app.agents.order_agent import process_orders
from app.agents.qa_agent import qa_check
from app.agents.reporter_agent import generate_report
from app.utils.io import read_csv, write_json, write_csv

def run(catalog_path, orders_path, out_path, listing_llm, qa_llm):
    print("🚀 Starting pipeline...")

    catalog = read_csv(catalog_path)
    orders = read_csv(orders_path)

    print("📦 Selecting products...")
    products = select_products(catalog)
    write_json(products, f"{out_path}/selection.json")

    print("🧠 Generating listings...")
    listings = generate_listings(products, listing_llm)
    write_json(listings, f"{out_path}/listings.json")

    print("💰 Pricing...")
    price_df = pricing(products)
    write_csv(price_df, f"{out_path}/price_update.csv")
    write_csv(price_df[["sku", "stock"]], f"{out_path}/stock_update.csv")

    print("📦 Orders...")
    order_actions = process_orders(orders, products)
    write_json(order_actions, f"{out_path}/order_actions.json")

    print("🛡 QA...")
    issues = qa_check(listings, qa_llm)
    write_json(issues, f"{out_path}/listing_redlines.json")

    print("📝 Report...")
    report = generate_report(products, orders, issues)
    with open(f"{out_path}/daily_report.md", "w") as f:
        f.write(report)

    print("✅ DONE")