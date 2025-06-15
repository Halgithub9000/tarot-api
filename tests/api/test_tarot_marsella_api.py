from fastapi.testclient import TestClient
from app.api.api_tarot_marsella import app

client = TestClient(app)


def test_draw_cards_endpoint():
    response = client.get("/draw-cards?num_cards=4")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 4
    for card in data:
        assert "name" in card
        assert "suit" in card
        assert "meaning_up" in card
        assert "meaning_reversed" in card
        assert "is_reversed" in card
