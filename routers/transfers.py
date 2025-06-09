from fastapi import APIRouter, FastAPI
from models.schemas import TransferRequest

router = APIRouter(prefix="/transfer", tags=["Transfer"])

@router.post("/")
@router.post("/")
def initiate_transfer(req: TransferRequest):
    # You can read from a mock JSON db and update balances
    return {
        "status": "success",
        "transaction_id": "TXN123456",
        "message": f"Transferred ₹{req.amount} from {req.from_account} to {req.to_account}"
    }
