from app.models.oracle import Oracle
from app.schemas.spread import Spread


class OracleService:
    """
    Servicio de aplicación que orquesta la interpretación de tiradas.
    Recibe una tirada, delega al modelo Oracle y utiliza el LLMAdapter.
    """

    def __init__(self, oracle: Oracle):
        self.oracle = oracle

    def interpret_spread_in_detail(self, spread: Spread) -> str:
        """
        Orquesta la interpretación de la tirada usando el oráculo y el adaptador de LLM.
        """
        response = self.oracle.do_full_reading(spread)
        return response

    def interpret_spread(self, spread: Spread) -> str:
        """
        Orquesta la interpretación de la tirada usando el oráculo y el adaptador de LLM.
        """
        response = self.oracle.do_shallow_reading(spread)
        return response
