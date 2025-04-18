from fastapi import APIRouter
from app.api.v1.routes import fetch_stock_data

api_router = APIRouter()
api_router.include_router(fetch_stock_data.router)