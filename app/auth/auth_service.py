from fastapi import Request, HTTPException, Depends
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Definir el header para la API Key
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
print(str(api_key_header))
load_dotenv()


def verify_api_key(api_key: Optional[str] = Depends(api_key_header), request: Request = None):
    valid_key = os.getenv("API_SECRET_KEY")
    client_ip = request.client.host if request else "Unknown"

    # Rechaza si la API Key no es válida
    if api_key != valid_key:
        raise_authorization_error(client_ip, api_key)

    # Rechaza si la API Key no viene o viene vacía
    if not api_key or api_key.strip() == "" or api_key != valid_key:
        raise_authorization_error(client_ip, api_key)

    return api_key


def raise_authorization_error(host, api_key):
    logger.warning(
        "Intento de acceso no autorizado desde %s con API key: %s", host, api_key)
    raise HTTPException(
        status_code=403,
        detail="Acceso no autorizado. Se requiere una API Key válida.",
    )
