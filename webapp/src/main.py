import logging
import os
from logging import getLogger

from fastapi import APIRouter, FastAPI
from fastapi.openapi.docs import (get_redoc_html, get_swagger_ui_html,
                                  get_swagger_ui_oauth2_redirect_html)
from fastapi.staticfiles import StaticFiles

logging.basicConfig(level=logging.INFO)
logger = getLogger(__name__)

ENDPOINT_PREFIX = os.environ["ENDPOINT_PREFIX"]
logger.info(ENDPOINT_PREFIX)


# オフライン環境でも動作するようにdocs, redocのurlは自身で定義する
# 参考: https://fastapi.tiangolo.com/advanced/extending-openapi/#self-hosting-javascript-and-css-for-docs
app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=f"{ENDPOINT_PREFIX}/openapi.json",
)
app.mount("/static", StaticFiles(directory="static"), name="static")

router = APIRouter()


@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@router.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@router.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


@router.get("/users")
def read_main() -> list[int]:
    return [1, 2, 3]


app.include_router(router, prefix=ENDPOINT_PREFIX)
