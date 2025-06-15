
from app.models.card import Card


def test_card_fields():
    card = Card(
        name="El Mago",
        suit="Mayor",
        meaning_up="Habilidad",
        meaning_reversed="Manipulación",
        is_reversed=True
    )
    assert card.name == "El Mago"
    assert card.suit == "Mayor"
    assert card.is_reversed is True
