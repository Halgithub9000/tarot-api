
from app.services.tarot_service import MarsellaTarotService


def test_draw_cards_from_service():
    service = MarsellaTarotService()
    cards = service.draw_cards(5)
    assert len(cards) == 5
