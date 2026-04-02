def qa_check(listings, llm):
    prompt = f"""
    You are a QA agent.

    Check these Shopify listings:
    {listings}

    For each SKU, detect:
    - Overclaims (e.g. "best", "guaranteed")
    - Misleading specs
    - Missing important info

    Return STRICT JSON format:
    [
      {{
        "sku": "...",
        "issues": ["issue1", "issue2"]
      }}
    ]

    If no issues, return empty list.
    """

    res = llm.generate(prompt)

    return [{"raw": res}]