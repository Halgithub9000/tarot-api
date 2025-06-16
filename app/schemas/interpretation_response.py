from pydantic import BaseModel


class InterpretationResponse(BaseModel):
    interpretation: str
