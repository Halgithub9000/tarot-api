from fastapi import FastAPI
from app.services.tarot_service import MarsellaTarotService
from app.models.spread import Spread

app = FastAPI(title="Tarot API")


@app.get("/get-spread", response_model=Spread)
def spread_cards(num_cards: int = 3, intention: str = "general"):
    tarot_service = MarsellaTarotService()
    return tarot_service.spread_cards(num_cards, intention)
