from fastapi import APIRouter, HTTPException
import yfinance as yf
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/fetch_ticker_latest_price",
    tags=["fetch_ticker_latest_price"],
)

from fastapi import APIRouter, HTTPException, Query
import yfinance as yf
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/fetch_ticker_latest_price",
    tags=["fetch_ticker_latest_price"],
)

@router.get("")
async def fetch_ticker_latest_price(ticker: str = Query(..., description="The stock ticker symbol")):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=2)
    try:
        data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

        if data.empty:
            raise HTTPException(status_code=404, detail="Ticker not found or no data available for the given period")

        latest_data = data[['Close']]

        return {"ticker": ticker, "data": latest_data.to_dict(orient="records")}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
