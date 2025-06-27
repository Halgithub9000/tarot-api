from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

load_dotenv()
limiter = Limiter(key_func=lambda request: "global")


def create_app() -> FastAPI:
    app = FastAPI(title="Tarot API")

    # Configuración de slowapi
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    frontend_origin = os.getenv("FRONTEND_ORIGIN")
    origins = [
        frontend_origin
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Montar la carpeta de archivos estáticos
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    from app.api.api_oraculo import api_oraculo
    from app.api.api_tarot_marsella import api_tarot

    app.include_router(api_oraculo)
    app.include_router(api_tarot)
    return app


app = create_app()
