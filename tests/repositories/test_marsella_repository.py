from app.repositories.tarot_repository import MarsellaTarotRepository
from app.models.card import Card


def test_repository_returns_full_deck():
    repo = MarsellaTarotRepository()
    cards = repo.get_cards()
    assert isinstance(cards, list)
    assert len(cards) == 77
    assert all(isinstance(card, Card) for card in cards)
    assert any(card.name == "El Mago" for card in cards)
