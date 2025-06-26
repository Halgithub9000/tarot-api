import os
from dotenv import load_dotenv
from app.schemas.spread import Spread
from app.adapters.llm_adapter import LLMDedpseekR10528Adapter


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
        question = "Actúa como una tarotista sabia y empática," \
            "que interpreta las cartas de forma comprensiva, cercana y en correcto español a "\
            "un consultante del tarot buscando guía y claridad sobre su vida."\
            "Con base las cartas e intención que te proporcionaré, "\
            "entrega una interpretación detallada, en no más de 500 palabras , escrita en un lenguaje natural, cálido y humano."\
            "La interpretación debe abordar posibles situaciones actuales de la persona, "\
            "aprendizajes que está viviendo, y consejos o advertencias para su camino."  \
            "No seas determinista, sino orientadora; deja espacio a la reflexión y al libre albedrío."\
            "Evita lenguaje mecánico o robótico. Usa un tono similar al de una tarotista real:" \
            "profundo, intuitivo, amable.\n"
        prompt = self.build_prompt(spread, question)
        return self.llm_adapter.generate_interpretation(prompt)

    def do_shallow_reading(self, spread: Spread) -> str:
        question = "Actúa como una tarotista sabia y empática. Realiza una interpretación del " \
            "tarot en no más de 250 palabras, usando un lenguaje cálido e intuitivo. " \
            "Instrucciones: " \
            "- Interpreta el significado de cada carta " \
            "- Conecta las cartas en una narrativa fluida " \
            "- Ofrece consejos prácticos pero no deterministas " \
            "- Mantén un tono cercano y comprensivo " \
            "- Invita a la reflexión personal " \
            "- Evita lenguaje técnico o impersonal  " \
            "- Usa un lenguaje natural y cercano como si hablaras directamente a la persona" \
            "- Exprésate en segunda persona"

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

        print(prompt)

        return prompt
