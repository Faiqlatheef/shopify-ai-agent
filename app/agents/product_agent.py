def select_products(df):
    df = df[df["stock"] >= 10]
    return df.head(10).to_dict(orient="records")