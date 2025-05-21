import os
from typing import Annotated, List, Optional, Union
from loguru import logger
from fastapi import APIRouter, HTTPException, Query, Request, Response
import requests

from src.adapters.driver.API.schemas.create_purchase_schema import CreatePurchaseSchema
from src.core.domain.aggregates.pedido_aggregate import PedidoAggregate
from src.core.domain.entities.compra_entity import CompraEntity

router = APIRouter(
    prefix="/pedido",
    tags=["Pedidos"],
)

PEDIDO_BASE_URL = os.getenv("PEDIDO_BASE_URL", "http://localhost:8001/pedido")


@router.get("/index")
async def list_pedidos(
    request: Request,
    status: Optional[int] = None,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
) -> Union[List[PedidoAggregate], None]:

    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PEDIDO_BASE_URL}/index",
            params={
                "status": status,
                "min_value": min_value,
                "max_value": max_value,
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


@router.post("/make")
async def create_pedido(request: Request, pedido: CreatePurchaseSchema) -> CompraEntity:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.post(
            f"{PEDIDO_BASE_URL}/make",
            json=pedido.model_dump(),
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


@router.get("/{pedido_id}")
async def get_pedido(request: Request, pedido_id: int) -> PedidoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PEDIDO_BASE_URL}/{pedido_id}",
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


@router.patch("/{pedido_id}/add_product/{product_id}")
async def add_new_product_to_pedido(
    request: Request, pedido_id: int, product_id: int
) -> CompraEntity:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.patch(
            f"{PEDIDO_BASE_URL}/{pedido_id}/add_product/{product_id}",
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


@router.patch("/{pedido_id}/{product_id}/add_component/{component_id}")
async def add_new_component_to_product_in_pedido(
    request: Request, pedido_id: int, product_id: int, component_id: int
) -> CompraEntity:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.patch(
            f"{PEDIDO_BASE_URL}/{pedido_id}/{product_id}/add_component/{component_id}",
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


@router.patch("/conclude/{pedido_id}")
async def concludes_pedido(request: Request, pedido_id: int) -> PedidoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.patch(
            f"{PEDIDO_BASE_URL}/conclude/{pedido_id}",
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


@router.patch("/cancel/{pedido_id}")
async def cancel_pedido(request: Request, pedido_id: int) -> PedidoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.patch(
            f"{PEDIDO_BASE_URL}/cancel/{pedido_id}",
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
