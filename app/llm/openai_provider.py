import os
from .base import LLMProvider

class OpenAIProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            return response.choices[0].message.content

        except Exception as e:
            # ✅ FALLBACK (IMPORTANT FOR $0 RUN)
            return self.mock_response(prompt)

    def mock_response(self, prompt: str) -> str:
        return """
        {
          "title": "High Quality Product",
          "bullets": ["Durable", "Affordable", "Best Seller"],
          "description": "This is a great product for everyday use.",
          "tags": ["shopify", "sale", "trending"]
        }
        """