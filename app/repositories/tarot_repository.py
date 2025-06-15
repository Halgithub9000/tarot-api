import json
from typing import List
from app.models.card import Card


class TarotRepository:
    def get_cards(self) -> List[Card]:
        raise NotImplementedError


class MarsellaTarotRepository(TarotRepository):
    def __init__(self):
        self.json_path = "app/data/marsella_cards.json"

    def get_cards(self) -> List[Card]:
        with open(self.json_path, encoding="utf-8") as f:
            data = json.load(f)
        return [Card(**card) for card in data]
