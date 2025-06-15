from abc import ABC, abstractmethod
from typing import List
from app.models.card import Card
from app.models.spread import Spread


class Deck(ABC):
    @abstractmethod
    def get_cards(self) -> List[Card]:
        pass

    def shuffle(self, cards: List[Card]) -> List[Card]:
        import random
        random.shuffle(cards)
        return cards

    def spread(self, n: int, intention: str) -> Spread:
        cards = self.get_cards()
        shuffled = self.shuffle(cards)
        drawn = shuffled[:n]
        import random
        for card in drawn:
            card.is_reversed = random.choice([True, False])
        spread = Spread(cards=drawn, intention=intention)
        return spread


class MarsellaDeck(Deck):
    def __init__(self, repository):
        self.repository = repository

    def get_cards(self) -> List[Card]:
        return self.repository.get_cards()
