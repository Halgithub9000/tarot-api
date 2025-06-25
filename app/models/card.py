import re
from pydantic import BaseModel, Field, field_validator


class Card(BaseModel):
    name: str = Field(..., max_length=30)
    suit: str = Field(..., max_length=10)
    meaning_up: str
    meaning_reversed: str
    is_reversed: bool = False
    image_url: str

    @field_validator("name", "suit", "meaning_up", "meaning_reversed")
    @classmethod
    def sanitize_intention(cls, value):
        # Elimina espacios al inicio y final
        value = value.strip()
        # Elimina caracteres no permitidos (solo letras, números, espacios y signos básicos)
        if not re.match(r"^[\w\s.,;:¡!¿?\-áéíóúÁÉÍÓÚüÜñÑ]+$", value):
            raise ValueError("Intention contiene caracteres no permitidos.")
        return value
