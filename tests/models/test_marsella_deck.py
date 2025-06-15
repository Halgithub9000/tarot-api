from app.models.deck import MarsellaDeck
from app.repositories.tarot_repository import MarsellaTarotRepository


def test_draw_cards_unique_and_reversed():
    repo = MarsellaTarotRepository()
    deck = MarsellaDeck(repo)
    drawn = deck.draw(3)
    assert len(drawn) == 3
    names = [card.name for card in drawn]
    assert len(names) == len(set(names))
    assert all(isinstance(card.is_reversed, bool) for card in drawn)
