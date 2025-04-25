from fastapi import APIRouter

router = APIRouter(
    prefix="/fetch_stock_data",
    tags=["fetch_stock_data"],
)
