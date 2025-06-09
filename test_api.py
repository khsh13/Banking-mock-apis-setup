from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/")
def hello():
    return {"message": "hi"}

app = FastAPI()
app.include_router(router)