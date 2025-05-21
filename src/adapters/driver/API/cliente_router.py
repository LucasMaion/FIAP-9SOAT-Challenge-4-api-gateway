import os
from typing import Union
from fastapi import APIRouter, HTTPException, Request, Response
from loguru import logger
import requests
from src.adapters.driver.API.schemas.create_client_schema import CreateClientSchema
from src.core.domain.aggregates.cliente_aggregate import ClienteAggregate

router = APIRouter(
    prefix="/cliente",
    tags=["Clientes"],
)

CLIENT_BASE_URL = os.getenv("CLIENT_BASE_URL", "http://localhost:8001/cliente")


@router.get("/{document}")
async def get_item_by_document(
    request: Request, document: str
) -> Union[ClienteAggregate, None]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{CLIENT_BASE_URL}/{document}", headers=forwarded_headers
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


@router.post("/", status_code=201)
async def create_client(
    request: Request,
    new_client: CreateClientSchema,
) -> Union[ClienteAggregate, None]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{CLIENT_BASE_URL}",
            json=new_client.model_dump(),
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
