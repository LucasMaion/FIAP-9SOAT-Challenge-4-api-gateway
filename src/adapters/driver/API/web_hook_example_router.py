import json
from fastapi import APIRouter, HTTPException
from loguru import logger
from src.adapters.driver.API.schemas.web_hook_example_schema import WebHookExampleSchema

router = APIRouter(
    prefix="/example/webhook",
    tags=["exemplos"],
)


@router.post("/")
async def initiate_payment(event: WebHookExampleSchema) -> None:
    try:
        logger.info("Received webhook event")
        logger.info(event)
        body = json.loads(event.message)
        logger.success("extracted body")
        logger.success(body)

    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))
