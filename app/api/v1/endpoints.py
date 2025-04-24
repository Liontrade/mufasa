from fastapi import APIRouter
from app.api.v1.routes import fetch_stock_data
from app.api.v1.routes import fetch_ticker_latest_price

api_router = APIRouter()
api_router.include_router(fetch_stock_data.router)
api_router.include_router(fetch_ticker_latest_price.router)