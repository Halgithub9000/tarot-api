from typing import Protocol
from abc import abstractmethod


class Prompt(Protocol):

    @abstractmethod
    def get_question(self) -> str: ...


class TarotReadingPrompt(Prompt):

    question = ""

    def get_question(self) -> str:
        """
        Devuelve el prompt para una lectura de tarot de tres cartas detallada."""
        return self.question


class TarotShallowReadingPrompt(TarotReadingPrompt):

    question = ("Haz una lectura de tarot de tres cartas concisa y práctica."
                "Sin introducciones extensas, menciona al inicio que no "
                "es una predicción sino una reflexión. "
                "Describe brevemente los símbolos de cada carta "
                "con un enfoque directo y su implicación práctica "
                "para la vida diaria. Utiliza un tono cercano y "
                "conversacional. La lectura debe ser clara, "
                "directa y no exceder 150 palabras. Evita lenguaje místico o complejo."

                )


class TarotFullReadingPrompt(TarotReadingPrompt):

    question = (
        "Realiza una lectura de tarot de tres cartas. "
        "La lectura no debe predecir el futuro, sino proponer una reflexión a "
        "partir de los símbolos. Desarrolla la interpretación de cada "
        "carta como parte de una narración íntima, con descripciones "
        "detalladas de símbolos y significados, conectándolos en una "
        "atmósfera cálida. Evita listas, encabezados o divisiones. "
        "La lectura debe sentirse como un relato, donde cada carta aparece "
        "como un capítulo que se enlaza con las demás. "
        "Finaliza con una conclusión que recoja el hilo de las "
        "tres cartas y sugiera una enseñanza para el día. Usa un lenguaje "
        "natural y evita estructuras típicas de IA."
    )
