from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel):
    age: int
    monthly_spend: int
    support_tickets: int
    usage_hours: int


@app.get("/")
def home():
    return {"message": "ML Churn Prediction System Running"}


@app.post("/predict-churn")
def predict_churn(customer: Customer):

    score = 0

    # -------------------------
    # Monthly spend impact
    # -------------------------
    if customer.monthly_spend < 500:
        score += 3
    elif customer.monthly_spend < 1500:
        score += 2

    # -------------------------
    # Support tickets impact
    # -------------------------
    if customer.support_tickets > 5:
        score += 3
    elif customer.support_tickets > 2:
        score += 2

    # -------------------------
    # Usage behavior impact
    # -------------------------
    if customer.usage_hours < 5:
        score += 3
    elif customer.usage_hours < 10:
        score += 2

    # -------------------------
    # Age factor (minor signal)
    # -------------------------
    if customer.age < 25 or customer.age > 50:
        score += 1

    # -------------------------
    # Final decision
    # -------------------------
    if score >= 7:
        prediction = "HIGH CHURN RISK"
    elif score >= 4:
        prediction = "MEDIUM CHURN RISK"
    else:
        prediction = "LOW CHURN RISK"

    return {
        "prediction": prediction,
        "risk_score": score,
        "customer_data": customer.dict()
    }