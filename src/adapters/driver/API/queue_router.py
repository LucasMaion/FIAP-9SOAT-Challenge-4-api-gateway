import os
from typing import List, Union
from fastapi import APIRouter, HTTPException, Request, Response
from loguru import logger
import requests

from src.core.domain.aggregates.pedido_aggregate import PedidoAggregate

router = APIRouter(
    prefix="/queue",
    tags=["Fila de Pedidos"],
)

QUEUE_BASE_URL = os.getenv("QUEUE_BASE_URL", "http://localhost:8001/queue")


@router.get("/")
async def get_queue(
    request: Request,
) -> Union[List[PedidoAggregate], None]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{QUEUE_BASE_URL}/",
            headers=forwarded_headers,
        )
        return Response(
            content=result.content,
            status_code=result.status_code,
            headers=result.headers,
        )
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/")
async def update_queue_item_status(
    request: Request, pedido_id: int, new_status_number: int
) -> PedidoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.put(
            f"{QUEUE_BASE_URL}/",
            json={
                "pedido_id": pedido_id,
                "new_status_number": new_status_number,
            },
            headers=forwarded_headers,
        )
        return Response(
            content=result.content,
            status_code=result.status_code,
            headers=result.headers,
        )
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))
