import json

def generate_listings(products, llm):
    prompt = f"""
    Generate Shopify listings for these products:
    {products}

    Return JSON list with:
    sku, title, bullets, description, tags
    """

    res = llm.generate(prompt)

    return [{"raw_output": res}]