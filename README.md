# 🛒 Shopify Dropshipping Multi-Agent AI System

## 🚀 Overview

This project implements a **multi-agent AI system** that simulates end-to-end Shopify dropshipping operations. It automates product sourcing, listing generation, pricing, order routing, QA validation, and reporting.

The system is designed to be:

* **Modular** (independent agents)
* **Deterministic-first** (reliable business logic)
* **Cost-efficient** (runs locally using Ollama)
* **Production-inspired** (clean architecture + CLI + UI)

---

# 🧠 Architecture

## 🔷 High-Level Flow

```
CLI / Streamlit UI
        ↓
   Manager Agent
        ↓
-------------------------------------------------
| Product Agent                                 |
| Listing Agent (LLM - llama3)                  |
| Pricing & Stock Agent                         |
| Order Routing Agent                           |
| QA Agent (LLM - mistral)                      |
| Reporter Agent                                |
-------------------------------------------------
        ↓
     Outputs (JSON / CSV / MD)
```

---

## 🔷 Component Responsibilities

### 🧩 Manager Agent

* Central orchestrator
* Controls workflow execution
* Passes data between agents
* Handles output generation

---

### 📦 Product Sourcing Agent

* Filters products with:

  * Stock ≥ 10
* Selects top 10 SKUs
* Outputs: `selection.json`

---

### 📝 Listing Agent (LLM – llama3)

* Generates:

  * Title
  * Bullet points
  * Description
  * Tags
* Uses **LLM for semantic content generation**
* Outputs: `listings.json`

---

### 💰 Pricing & Stock Agent

* Deterministic pricing logic
* Ensures ≥ 25% margin
* Applies:

  * Platform fees
  * GST
* Outputs:

  * `price_update.csv`
  * `stock_update.csv`

---

### 📦 Order Routing Agent

* Decides:

  * Fulfill / Backorder
* Generates customer emails
* Outputs: `order_actions.json`

---

### 🛡 QA Agent (LLM – mistral)

* Detects:

  * Overclaims
  * Misleading descriptions
  * Missing info
* Produces structured JSON per SKU
* Outputs: `listing_redlines.json`

---

### 📄 Reporter Agent

* Summarizes all system outputs
* Generates daily report
* Outputs: `daily_report.md`

---

## 🤖 Multi-LLM Architecture

| Agent         | Model   | Purpose            |
| ------------- | ------- | ------------------ |
| Listing Agent | llama3  | Content generation |
| QA Agent      | mistral | Validation & QA    |

* Runs via **Ollama**
* Fully local → **$0 cost**
* Demonstrates **multi-model orchestration**

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama

Download:
https://ollama.com

Run:

```bash
ollama serve
ollama pull llama3
ollama pull mistral
```

---

## ▶️ Run the System (CLI)

```bash
python -m app.main --catalog data/supplier_catalog.csv --orders data/orders.csv --out out/
```

---

## 🌐 Run UI (Optional)

```bash
python -m streamlit run app/ui.py
```

Access:
http://localhost:8501

---

## 📂 Outputs

Generated inside `/out/`:

* `selection.json` → Selected products
* `listings.json` → Generated listings
* `price_update.csv` → Pricing data
* `stock_update.csv` → Stock updates
* `order_actions.json` → Order decisions
* `listing_redlines.json` → QA issues
* `daily_report.md` → Summary report

---

## 💰 Pricing Logic

The system computes the **minimum price P** such that:

* Platform fee = `2.9% * P + $0.30`
* GST (AU) = `10% * P`
* Margin ≥ **25%**

Final price:

* Rounded to nearest `$0.50`

---

## 🧪 Design Decisions

* Deterministic logic for pricing & routing
* LLMs used selectively (content + QA)
* Batch prompting to reduce LLM calls
* Structured outputs for downstream usage

---

## ⚠️ Assumptions

* Supplier data is accurate
* All SKUs are valid
* No partial order fulfillment

---

## 🚧 Limitations

* No strict JSON schema validation
* No real Shopify API integration
* Basic QA rules

---

## 🔮 Future Improvements

* JSON schema enforcement
* LLM response caching
* Async processing
* Shopify API integration
* Advanced QA (rule + LLM hybrid)
* Monitoring & logging

---

## 🎯 Key Highlights

* Multi-agent architecture
* Multi-LLM integration
* Fully local ($0 cost)
* CLI + UI support
* Clean, scalable design

---

## 🏁 Conclusion

This system demonstrates how **AI agents can automate real-world e-commerce workflows** while balancing performance, cost, and scalability.

---
