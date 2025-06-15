from pydantic import BaseModel
from typing import List
from app.models.card import Card


class Spread(BaseModel):
    cards: List[Card]
    intention: str
