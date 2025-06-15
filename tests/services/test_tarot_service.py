
from app.services.tarot_service import TarotService


def test_draw_cards_from_service():
    service = TarotService()
    cards = service.draw_cards(5)
    assert len(cards) == 5


def test_invalid_deck_type_raises():
    try:
        TarotService(deck_type="waite")
    except ValueError:
        assert True
    else:
        assert False, "Debe lanzar ValueError para deck_type desconocido"
