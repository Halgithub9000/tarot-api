from app.models.deck import MarsellaDeck
from app.repositories.tarot_repository import MarsellaTarotRepository
from typing import Protocol


class TarotService(Protocol):

    def draw_cards(self, n: int):
        ...


class MarsellaTarotService(TarotService):
    def __init__(self):
        repo = MarsellaTarotRepository()
        self.deck = MarsellaDeck(repo)

    def draw_cards(self, n: int):
        return self.deck.draw(n)
