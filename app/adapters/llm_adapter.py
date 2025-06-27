import os
import anthropic
from typing import Protocol
from dotenv import load_dotenv
import requests


class LLMAdapter(Protocol):

    def generate_interpretation(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": self.model
        }

        response = requests.post(
            self.endpoint, headers=headers, json=payload, timeout=120)

        if response.status_code != 200:
            print(str(response.status_code))
            return f"Error: {response.status_code} - {response.text}"

        result = response.json()
        return self.clean_interpretation(result)

    def clean_interpretation(self, interpretation: str) -> str:
        """
        Limpia la interpretación eliminando elementos no deseados de la respuesta.
        """
        return interpretation.get("choices", [{}])[0].get("message", {}).get("content", "No content returned from LLM.")


class LLMMistralSmall2506Adapter(LLMAdapter):
    """
    Adaptador para el modelo Magistral-Small-2506 vía Hugging Face Inference API.
    """

    def __init__(self, api_key: str):
        load_dotenv()
        model = os.getenv("HF_MAGISTRAL-SMALL-2506_MODEL_ID")
        endpoint = os.getenv("HF_MAGISTRAL-SMALL-2506_ENDPOINT")
        self.api_key = api_key
        self.model = model
        self.endpoint = endpoint


class LLMDedpseekR10528Adapter(LLMAdapter):
    """
    Adaptador para el modelo Dedpseek-R10528 vía Hugging Face Inference API.
    """

    def __init__(self, api_key: str):
        load_dotenv()
        model = os.getenv("HF_DEEPSEEK-R1-0528-MODEL-ID")
        endpoint = os.getenv("HF_DEEPSEEK-R1-0528-ENDPOINT")
        self.api_key = api_key
        self.model = model
        self.endpoint = endpoint


class LLMClaudeHaiku35Adapter(LLMAdapter):
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("ANTHROPIC_TOKEN")
        self.model = os.getenv("ANTHROPIC_CLAUDE_35_HAIKU_MODEL")
        self.endpoint = os.getenv("ANTHROPIC_CLAUDE_35_HAIKU_ENDPOINT")
        self.max_tokens = 8192
        self.temperature = 1.0

    def generate_interpretation(self, prompt: str) -> str:
        client = anthropic.Anthropic(api_key=self.api_key)

        try:
            message = client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            # El contenido de la respuesta está en message.content
            return message.content[0].text if message.content else "No content returned from Claude."
        except Exception as e:
            print(f"Anthropic API error: {e}")
            return f"Error: {e}"
