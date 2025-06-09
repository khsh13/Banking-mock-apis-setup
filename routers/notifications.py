from fastapi import APIRouter, FastAPI
from models.schemas import NotificationRequest

router = APIRouter(prefix="/notify", tags=["Notifications"])

@router.post("/")
def send_message(req: NotificationRequest):
    print(f"[Mock SMS] Sent to {req.user_id}: {req.message}")
    return {"status": "delivered"}
