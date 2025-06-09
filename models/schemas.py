from pydantic import BaseModel

class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: float

class FraudCheckRequest(BaseModel):
    transaction_id: str
    amount: float
    location: str
    time: str

class NotificationRequest(BaseModel):
    user_id: str
    message: str
