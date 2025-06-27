from fastapi import Depends, Request, APIRouter
from app.main import limiter
from app.schemas.spread import Spread
from app.services.oracle_service import OracleService
from app.models.oracle import Oracle
from app.schemas.interpretation_response import InterpretationResponse
from app.auth.auth_service import verify_api_key

api_oraculo = APIRouter(tags=["oraculo"])


@api_oraculo.post("/oracle/interpret-in-detail", response_model=InterpretationResponse)
@limiter.limit("10/minute")
def interpret_spread_in_detail(request: Request, spread_request: Spread):
    oracle = Oracle()
    oracle_service = OracleService(oracle)
    interpretation = oracle_service.interpret_spread_in_detail(spread_request)
    interpretation_response = InterpretationResponse(
        interpretation=interpretation)
    return interpretation_response


@api_oraculo.post("/oracle/interpret-superficially", response_model=InterpretationResponse)
@limiter.limit("10/minute")
def interpret_spread_superficially(request: Request, spread_request: Spread):
    oracle = Oracle()
    oracle_service = OracleService(oracle)
    interpretation = oracle_service.interpret_spread(spread_request)
    interpretation_response = InterpretationResponse(
        interpretation=interpretation)
    return interpretation_response
