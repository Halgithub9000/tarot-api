import os
from dotenv import load_dotenv
from app.schemas.spread import Spread
from app.adapters.llm_adapter import LLMAdapter, LLMDedpseekR10528Adapter


class Oracle:
    """
    Representa un Oráculo capaz de interpretar tiradas de cartas utilizando un modelo de lenguaje (LLM).
    """

    def __init__(self, name: str = "Oráculo Marsella"):
        load_dotenv()
        HF_TOKEN = os.getenv("HF_TOKEN")
        self.name = name
        self.llm_adapter = LLMDedpseekR10528Adapter(HF_TOKEN)

    def do_full_reading(self, spread: Spread) -> str:
        question = "Actúa como alguien que sabe leer el tarot en español e interpreta mi tarot diario de 3 cartas. "\
            "Utiliza un tono amable y ligeramente informal para que la interpretación sea más cercana y comprensible. "\
            "La tirada no es adivinatoria, sino que enfocada en un consejo a partir de los simbolos de cada carta."\
            "Enfócate principalmente en la intención que señalaré luego y suma a la interpretación de cada carta una "\
            "descripción de sus símbolos. Haz la interpretacón de forma detallada"

        prompt = self.build_prompt(spread, question)
        return self.llm_adapter.generate_interpretation(prompt)

    def do_shallow_reading(self, spread: Spread) -> str:
        question = "Actúa como alguien que sabe leer el tarot en español e interpreta mi tarot diario de 3 cartas. "\
            "Utiliza un tono amable y ligeramente informal para que la interpretación sea más cercana y comprensible. " \
            "Haz la interpretacion de la manera resumida más resumida posible" \
            "Enfócate principalmente en la intención que señalaré a continuación : "

        prompt = self.build_prompt(spread, question)
        return self.llm_adapter.generate_interpretation(prompt)

    def build_prompt(self, spread: Spread, question: str) -> str:
        """
        Construye el prompt textual que será enviado al modelo de lenguaje.
        Incluye el nombre, versión, descripción del oráculo, intención de la tirada y descripción de las cartas.
        """

        cards_names = ", ".join(card.name + (" (invertida)" if card.is_reversed else "(al derecho)")
                                for card in spread.cards)

        promptfinal = question + "Intención de la tirada: " + \
            spread.intention + " Cartas: " + cards_names

        return promptfinal
