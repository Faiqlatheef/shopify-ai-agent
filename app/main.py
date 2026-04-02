import argparse
import os
from app.manager import run
from app.llm.ollama_provider import OllamaProvider

def main():
    print("🔥 Starting main...")  # debug

    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog")
    parser.add_argument("--orders")
    parser.add_argument("--out")

    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    listing_llm = OllamaProvider(model="llama3")
    qa_llm = OllamaProvider(model="mistral")

    run(args.catalog, args.orders, args.out, listing_llm, qa_llm)


# 🚨 THIS LINE MUST EXIST
if __name__ == "__main__":
    main()