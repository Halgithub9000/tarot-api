from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.tarot_service import MarsellaTarotService
from app.schemas.spread import Spread
from app.services.oracle_service import OracleService
from app.models.oracle import Oracle
from app.schemas.interpretation_response import InterpretationResponse


app = FastAPI(title="Tarot API")
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Solo permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-spread", response_model=Spread)
def spread_cards(num_cards: int = 3, intention: str = "general"):
    tarot_service = MarsellaTarotService()
    return tarot_service.spread_cards(num_cards, intention)


@app.post("/oracle/interpret-in-detail", response_model=InterpretationResponse)
def interpret_spread_in_detail(spread_request: Spread):
    # Convertir CardRequest a Card (modelo de dominio)
    spread = Spread(cards=spread_request.cards,
                    intention=spread_request.intention)
    oracle = Oracle()
    # llm_adapter = LLMMistralSmall2506Adapter(HF_TOKEN)
    oracle_service = OracleService(oracle)
    interpretation = oracle_service.interpret_spread_in_detail(spread)
    interpretation_response = InterpretationResponse(
        interpretation=interpretation)
    return interpretation_response


@app.post("/oracle/interpret-superficially", response_model=InterpretationResponse)
def interpret_spread_superficially(spread_request: Spread):
    # Convertir CardRequest a Card (modelo de dominio)
    spread = Spread(cards=spread_request.cards,
                    intention=spread_request.intention)
    oracle = Oracle()
    # llm_adapter = LLMMistralSmall2506Adapter(HF_TOKEN)
    oracle_service = OracleService(oracle)
    interpretation = oracle_service.interpret_spread(spread)
    interpretation_response = InterpretationResponse(
        interpretation=interpretation)
    return interpretation_response
