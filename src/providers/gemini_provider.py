import os
from google import genai
class GeminiProvider:
    def __init__(self, model_name="gemini-2.5-flash"):
        self.model_name = model_name
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is missing from environment variables.")
        self.client = genai.Client(api_key=self.api_key)
    def generate_response(self, payload: str) -> str:
        try:
            # Applying basic constraints as per security model (budget/rate proxy via max_output_tokens)
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=payload,
                config=genai.types.GenerateContentConfig(
                    max_output_tokens=200, 
                    temperature=0.0
                )
            )
            return response.text if response.text else "Empty response from Gemini."
        except Exception as e:
            return f"PROVIDER_ERROR: {str(e)}"
