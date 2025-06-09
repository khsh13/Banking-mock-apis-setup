from fastapi import APIRouter, FastAPI
from models.schemas import FraudCheckRequest
from utils.fraud_rules import is_suspicious

router = APIRouter(prefix="/fraud-check", tags=["Fraud Check"])

@router.post("/")
def check_fraud(req: FraudCheckRequest):
    result = is_suspicious(req.amount, req.location, req.time)
    return {
        "transaction_id": req.transaction_id,
        "is_fraud": result
    }
def is_suspicious(amount, location, time):
    if amount > 100000 or location not in ["IN", "US", "UK"]:
        return True
    return False
