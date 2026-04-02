# Shopify Dropshipping Multi-Agent System

## Overview

This project implements a multi-agent AI system that simulates Shopify dropshipping operations including product selection, listing generation, pricing, order routing, QA, and reporting.

The system is designed to be:

* Modular (multi-agent architecture)
* Cost-efficient (runs fully locally using Ollama)
* Deterministic where needed (pricing, stock)
* Scalable and production-friendly

---

## Architecture

Manager Agent orchestrates the following agents:

1. Product Sourcing Agent → selects top SKUs
2. Listing Agent (LLM - llama3) → generates product content
3. Pricing & Stock Agent → calculates prices (≥25% margin)
4. Order Routing Agent → decides fulfillment/backorder
5. QA Agent (LLM - mistral) → detects listing issues
6. Reporter Agent → generates daily report

---

## Multi-LLM Setup

* llama3 → Listing generation
* mistral → QA validation

Both run locally using Ollama (no API cost).

---

## Setup Instructions

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download: https://ollama.com

Run:

```bash
ollama serve
ollama pull llama3
ollama pull mistral
```

---

## Run the System

```bash
python -m app.main --catalog data/supplier_catalog.csv --orders data/orders.csv --out out/
```

---

## Outputs

The system generates:

* selection.json
* listings.json
* price_update.csv
* stock_update.csv
* order_actions.json
* listing_redlines.json
* daily_report.md

---

## Pricing Logic

Ensures:

* Platform fee = 2.9% + $0.30
* GST (AU) = 10%
* Minimum margin ≥ 25%
* Rounded to nearest $0.50

---

## Assumptions

* All products are valid for Shopify listing
* Supplier stock is accurate
* Simple order routing logic used

---

## Limitations

* LLM output not strictly structured (no schema enforcement)
* No real Shopify API integration
* Basic QA rules

---

## Future Improvements

* Add JSON validation
* Add caching for LLM calls
* Integrate Shopify API
* Improve prompt engineering
* Add async processing

---

## Design Philosophy

The system prioritizes:

* Simplicity
* Determinism where possible
* Efficient LLM usage
* Clear separation of responsibilities

---

## Key Highlight

This solution satisfies the $0 cost constraint by using local LLMs via Ollama while still implementing a true multi-agent architecture.

---
