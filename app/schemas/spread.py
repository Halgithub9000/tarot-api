import re
from pydantic import BaseModel, field_validator, Field
from typing import List
from app.models.card import Card


class Spread(BaseModel):
    cards: List[Card]
    intention: str = Field(..., max_length=100)

    @field_validator("intention")
    @classmethod
    def sanitize_intention(cls, value):
        # Elimina espacios al inicio y final
        value = value.strip()
        # Elimina caracteres no permitidos (solo letras, números, espacios y signos básicos)
        if not re.match(r"^[\w\s.,;:¡!¿?\-áéíóúÁÉÍÓÚüÜñÑ]+$", value):
            raise ValueError("Intention contiene caracteres no permitidos.")
        return value
