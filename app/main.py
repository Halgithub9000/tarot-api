from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=lambda request: "global")


def create_app() -> FastAPI:
    app = FastAPI(title="Tarot API")

    # Configuración de slowapi
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    # (Descomenta y ajusta si necesitas CORS)
    # origins = [
    #    "http://localhost:5173",
    #    "http://localhost:3000",
    #    "http://127.0.0.1",
    #    "http://127.0.0.1:3000"

    # ]
    # app.add_middleware(
    #    CORSMiddleware,
    #    allow_origins=origins,
    #    allow_credentials=True,
    #    allow_methods=["*"],
    #    allow_headers=["*"],
    # )

    from app.api.api_oraculo import api_oraculo
    from app.api.api_tarot_marsella import api_tarot

    app.include_router(api_oraculo)
    app.include_router(api_tarot)
    return app


app = create_app()
