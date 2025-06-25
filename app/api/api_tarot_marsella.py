from fastapi import Depends, Request, APIRouter
from app.main import limiter
from app.services.tarot_service import MarsellaTarotService
from app.schemas.spread import Spread
from app.auth.auth_service import verify_api_key

api_tarot = APIRouter(tags=["tarot"])


@api_tarot.get("/get-spread", response_model=Spread)
@limiter.limit("5/minute")
def spread_cards(request: Request, num_cards: int = 3, intention: str = "general"):
    tarot_service = MarsellaTarotService()
    return tarot_service.spread_cards(num_cards, intention)
