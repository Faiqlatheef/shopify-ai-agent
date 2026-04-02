import streamlit as st
import os
import json
from app.manager import run
from app.llm.ollama_provider import OllamaProvider

# ✅ Page config
st.set_page_config(page_title="Shopify AI Ops", layout="wide")

# ✅ Title
st.title("🛒 Shopify Dropshipping AI Agent")
st.caption("Multi-Agent System for Automated Shopify Operations")

# -------------------------------
# 📌 Sidebar Controls
# -------------------------------
st.sidebar.header("⚙️ Configuration")

catalog = st.sidebar.text_input("Catalog Path", "data/supplier_catalog.csv")
orders = st.sidebar.text_input("Orders Path", "data/orders.csv")
out = st.sidebar.text_input("Output Folder", "out/")

run_btn = st.sidebar.button("🚀 Run System")

# -------------------------------
# 📊 Main Layout
# -------------------------------
col1, col2 = st.columns(2)

# LEFT PANEL
with col1:
    st.subheader("📂 System Inputs")
    st.write(f"📦 Catalog: `{catalog}`")
    st.write(f"🧾 Orders: `{orders}`")

# RIGHT PANEL
with col2:
    st.subheader("📁 Output Folder")
    st.write(f"📁 `{out}`")

# -------------------------------
# 🚀 Run Pipeline
# -------------------------------
if run_btn:
    st.info("⏳ Running AI pipeline... Please wait")

    listing_llm = OllamaProvider(model="llama3")
    qa_llm = OllamaProvider(model="mistral")

    os.makedirs(out, exist_ok=True)

    run(catalog, orders, out, listing_llm, qa_llm)

    st.success("✅ Pipeline Completed!")

# -------------------------------
# 📊 Output Display Section
# -------------------------------
if os.path.exists(out):

    st.markdown("---")
    st.header("📊 Results Dashboard")

    tabs = st.tabs([
        "📦 Products",
        "📝 Listings",
        "💰 Pricing",
        "📦 Orders",
        "🛡 QA",
        "📄 Report"
    ])

    # 📦 PRODUCTS
    with tabs[0]:
        if os.path.exists(f"{out}/selection.json"):
            st.json(json.load(open(f"{out}/selection.json")))

    # 📝 LISTINGS
    with tabs[1]:
        if os.path.exists(f"{out}/listings.json"):
            st.json(json.load(open(f"{out}/listings.json")))

    # 💰 PRICING
    with tabs[2]:
        if os.path.exists(f"{out}/price_update.csv"):
            st.dataframe(
                __import__("pandas").read_csv(f"{out}/price_update.csv")
            )

    # 📦 ORDERS
    with tabs[3]:
        if os.path.exists(f"{out}/order_actions.json"):
            st.json(json.load(open(f"{out}/order_actions.json")))

    # 🛡 QA
    with tabs[4]:
        if os.path.exists(f"{out}/listing_redlines.json"):
            st.json(json.load(open(f"{out}/listing_redlines.json")))

    # 📄 REPORT
    with tabs[5]:
        if os.path.exists(f"{out}/daily_report.md"):
            st.markdown(open(f"{out}/daily_report.md").read())