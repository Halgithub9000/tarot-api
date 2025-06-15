from app.models.deck import MarsellaDeck
from app.repositories.tarot_repository import MarsellaTarotRepository
from typing import Protocol


class TarotService(Protocol):

    def spread_cards(self, n: int):
        ...


class MarsellaTarotService(TarotService):
    def __init__(self):
        repo = MarsellaTarotRepository()
        self.deck = MarsellaDeck(repo)

    def spread_cards(self, n: int, intention: str):
        return self.deck.spread(n, intention)
