from abc import ABC, abstractmethod
from typing import List
from app.models.card import Card


class Deck(ABC):
    @abstractmethod
    def get_cards(self) -> List[Card]:
        pass

    def shuffle(self, cards: List[Card]) -> List[Card]:
        import random
        random.shuffle(cards)
        return cards

    def draw(self, n: int) -> List[Card]:
        cards = self.get_cards()
        shuffled = self.shuffle(cards)
        drawn = shuffled[:n]
        import random
        for card in drawn:
            card.is_reversed = random.choice([True, False])
        return drawn


class MarsellaDeck(Deck):
    def __init__(self, repository):
        self.repository = repository

    def get_cards(self) -> List[Card]:
        return self.repository.get_cards()
