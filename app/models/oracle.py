import os
from dotenv import load_dotenv
from app.schemas.spread import Spread
from app.models.prompt import TarotFullReadingPrompt, TarotShallowReadingPrompt
from app.adapters.llm_adapter import LLMClaudeHaiku35Adapter


class Oracle:
    """
    Representa un Oráculo capaz de interpretar tiradas de cartas utilizando un modelo de lenguaje (LLM).
    """

    def __init__(self, name: str = "Oráculo Marsella"):
        load_dotenv()
        self.name = name
        self.llm_adapter = LLMClaudeHaiku35Adapter()

    def do_full_reading(self, spread: Spread) -> str:
        question = TarotFullReadingPrompt().get_question()
        prompt = self.build_prompt(spread, question)
        return self.llm_adapter.generate_interpretation(prompt)

    def do_shallow_reading(self, spread: Spread) -> str:
        question = TarotShallowReadingPrompt().get_question()
        prompt = self.build_prompt(spread, question)
        return self.llm_adapter.generate_interpretation(prompt)

    def build_prompt(self, spread: Spread, question: str) -> str:
        """
        Construye el prompt textual que será enviado al modelo de lenguaje.
        Incluye el nombre, versión, descripción del oráculo, intención de la tirada y descripción de las cartas.
        """

        card_names = "\n".join(
            f"{idx+1}. {card.name} {'(invertida)' if card.is_reversed else '(al derecho)'}"
            for idx, card in enumerate(spread.cards)
        )

        prompt = (
            f"{question}\n"
            f"Cartas e intención : \n{card_names}\n"
            f"Intención: {spread.intention}"
        )

        return prompt
