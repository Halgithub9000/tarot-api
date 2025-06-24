from pydantic import BaseModel


class Card(BaseModel):
    name: str
    suit: str
    meaning_up: str
    meaning_reversed: str
    is_reversed: bool = False
    image_url: str
