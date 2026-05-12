import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from contextlib import asynccontextmanager
import redis


def seed_redis(redis_client):
    if not redis_client.exists("STUDENT10"):
        redis_client.set("STUDENT10", 10)
        redis_client.set("BIGSALE", 30)


@asynccontextmanager
async def lifespan(app: FastAPI):
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    r_client = redis.from_url(REDIS_URL, decode_responses=True)

    seed_redis(r_client)

    app.state.redis = r_client
    yield
    r_client.close()


app = FastAPI(title="Discount Service", lifespan=lifespan)


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    promo_code: Optional[str] = None


class DiscountResponse(BaseModel):
    discount_percent: float
    discount_amount: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
async def calculate_discount(request: DiscountRequest):
    r = app.state.redis
    discount_percent = 0
    reason = "No discount applied"
    if request.promo_code:
        stored_discount = r.get(request.promo_code)
        if stored_discount:
            discount_percent = int(stored_discount)
            reason = f"Promo code '{request.promo_code}' applied"

    if discount_percent == 0 and request.quantity >= 10:
        discount_percent = 5
        reason = "Discount for (10+ items)"

    total_price = request.price * request.quantity
    discount_amount = total_price * (discount_percent / 100)

    return {
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "reason": reason,
    }
