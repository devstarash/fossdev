import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="Discount Service",
)

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    promo_code: Optional[str] = None


class DiscountResponse(BaseModel):
    discount_percent: float
    discount_amount: float
    applied_reason: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}

@app.post("/discounts/calculate", response_model=DiscountResponse)
async def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    discount_percent = 0.0
    reason = "No discount applied"


    if request.promo_code == "STUDENT10":
        discount_percent = 10.0
        reason = "Student promo code"
    
  
    elif request.quantity >= 5:
        discount_percent = 15.0
        reason = "Wholesale discount"

    total_before = request.price * request.quantity
    discount_amount = total_before * (discount_percent / 100)

    return DiscountResponse(
        discount_percent=discount_percent,
        discount_amount=round(discount_amount, 2),
        applied_reason=reason,
    )