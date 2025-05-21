import os
from typing import List, Optional, Union
from fastapi import APIRouter, HTTPException, Request, Response
from loguru import logger
import requests

from src.adapters.driver.API.schemas.create_product_schema import CreateProductSchema
from src.adapters.driver.API.schemas.update_product_schema import UpdateProductSchema
from src.core.domain.aggregates.produto_aggregate import ProdutoAggregate
from src.core.domain.entities.categoria_entity import (
    CategoriaEntity,
)

router = APIRouter(
    prefix="/produto",
    tags=["Produtos"],
)

PRODUTO_BASE_URL = os.getenv("PRODUTO_BASE_URL", "http://localhost:8003/produto")


@router.get("/categories")
async def list_categories(
    request: Request,
) -> Union[List[CategoriaEntity], None]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PRODUTO_BASE_URL}/categories",
            headers=forwarded_headers,
        )
        return Response(
            content=result.content,
            status_code=result.status_code,
            headers=forwarded_headers,
        )
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/index")
async def list_itens(
    request: Request,
    name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
) -> Union[List[ProdutoAggregate], None]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PRODUTO_BASE_URL}/index",
            params={
                "name": name,
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
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


@router.get("/{item_id}")
async def get_item(request: Request, item_id: int) -> Union[ProdutoAggregate, None]:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.get(
            f"{PRODUTO_BASE_URL}/{item_id}",
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


@router.post("/", status_code=201)
async def create_item(
    request: Request, produto: CreateProductSchema
) -> ProdutoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.post(
            f"{PRODUTO_BASE_URL}/",
            json=produto.model_dump(),
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
async def update_item(
    request: Request, produto: UpdateProductSchema
) -> ProdutoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.put(
            f"{PRODUTO_BASE_URL}/",
            json=produto.model_dump(),
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


@router.delete("/{item_id}")
async def delete_item(request: Request, item_id: int):
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        requests.delete(
            f"{PRODUTO_BASE_URL}/{item_id}",
            headers=forwarded_headers,
        )
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/activate/{item_id}")
async def activate_item(request: Request, item_id: int) -> ProdutoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.patch(
            f"{PRODUTO_BASE_URL}/activate/{item_id}",
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


@router.patch("/deactivate/{item_id}")
async def deactivate_item(request: Request, item_id: int) -> ProdutoAggregate:
    try:
        forwarded_headers = {key: value for key, value in request.headers.items()}
        result = requests.patch(
            f"{PRODUTO_BASE_URL}/deactivate/{item_id}",
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
