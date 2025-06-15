from fastapi import FastAPI
from app.services.tarot_service import MarsellaTarotService
from app.models.card import Card
from typing import List

app = FastAPI(title="Tarot API")


@app.get("/draw-cards", response_model=List[Card])
def draw_cards(num_cards: int = 3):
    tarot_service = MarsellaTarotService()
    return tarot_service.draw_cards(num_cards)
