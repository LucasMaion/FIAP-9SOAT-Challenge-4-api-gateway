import os
from typing import Literal
from fastapi import APIRouter, HTTPException, Request
from loguru import logger
import requests

router = APIRouter(
    prefix="/maintenance",
    tags=["maintenance"],
)

PAYMENT_MAINTENANCE_BASE_URL = os.getenv(
    "PAYMENT_MAINTENANCE_BASE_URL", "http://localhost:8002/payment/maintenance"
)
PRODUTO_MAINTENANCE_BASE_URL = os.getenv(
    "PRODUTO_MAINTENANCE_BASE_URL", "http://localhost:8003/produto/maintenance"
)
PEDIDO_MAINTENANCE_BASE_URL = os.getenv(
    "PEDIDO_MAINTENANCE_BASE_URL", "http://localhost:8001/pedido/maintenance"
)


@router.post("/build_db/{service}", include_in_schema=False)
async def build_db_api(
    request: Request, service: Literal["payment", "produto", "pedido"]
) -> bool:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        if service == "payment":
            url = f"{PAYMENT_MAINTENANCE_BASE_URL}/build_db"
        elif service == "produto":
            url = f"{PRODUTO_MAINTENANCE_BASE_URL}/build_db"
        elif service == "pedido":
            url = f"{PEDIDO_MAINTENANCE_BASE_URL}/build_db"
        else:
            raise HTTPException(status_code=400, detail="Invalid service")
        result = requests.post(
            url,
            headers=forwarded_headers,
        )
        return True if result.status_code == 200 else False
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/seed_db/{service}", include_in_schema=False)
async def seed_db_api(
    request: Request, service: Literal["payment", "produto", "pedido"]
) -> bool:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        if service == "payment":
            url = f"{PAYMENT_MAINTENANCE_BASE_URL}/seed_db"
        elif service == "produto":
            url = f"{PRODUTO_MAINTENANCE_BASE_URL}/seed_db"
        elif service == "pedido":
            url = f"{PEDIDO_MAINTENANCE_BASE_URL}/seed_db"
        else:
            raise HTTPException(status_code=400, detail="Invalid service")
        result = requests.post(
            url,
            headers=forwarded_headers,
        )
        return True if result.status_code == 200 else False
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))
