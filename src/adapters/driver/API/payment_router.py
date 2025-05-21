import json
import os
from fastapi import APIRouter, HTTPException, Request, Response
from loguru import logger
from peewee import DoesNotExist
import requests
from src.adapters.driver.API.schemas.create_payment_schema import CreatePaymentSchema
from src.core.domain.aggregates.pagamento_aggregate import PagamentoAggregate
from src.core.domain.entities.meio_de_pagamento_entity import MeioDePagamentoEntity

router = APIRouter(
    prefix="/payment",
    tags=["Pagamentos"],
)

PAYMENT_BASE_URL = os.getenv("PAYMENT_BASE_URL", "http://localhost:8002/payment")


@router.post("/pay")
async def initiate_payment(
    request: Request, payment: CreatePaymentSchema
) -> PagamentoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.post(
            f"{PAYMENT_BASE_URL}/pay",
            json=payment.model_dump(),
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


@router.get("/methods")
async def list_payment_methods(
    request: Request,
) -> list[MeioDePagamentoEntity]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PAYMENT_BASE_URL}/methods",
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


@router.get("/{payment_id}")
async def get_payment(request: Request, payment_id: str) -> PagamentoAggregate | None:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PAYMENT_BASE_URL}/{payment_id}",
            headers=forwarded_headers,
        )
        return Response(
            content=result.content,
            status_code=result.status_code,
            headers=result.headers,
        )
    except DoesNotExist as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail="Item não localizado")
    except (ValueError, AttributeError, DoesNotExist) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(type(e))
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))
