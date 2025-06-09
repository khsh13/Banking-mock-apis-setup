from fastapi import FastAPI, APIRouter
from routers import transfers, fraud_check, notifications

app = FastAPI()

# ✅ Optional homepage route
@app.get("/")
def root():
    return {"message": "Welcome to Banking AI APIs"}

# ✅ Include your routers here
app.include_router(transfers.router, prefix="/transfer", tags=["Transfer"])
app.include_router(fraud_check.router, prefix="/fraud-check", tags=["Fraud Detection"])
app.include_router(notifications.router, prefix="/notify", tags=["Notifications"])
