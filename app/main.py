from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class HealthResponse(BaseModel):
    status: str
    message: str
@app.get("/")
def root():
    return {"message": "FastAPI 项目启动成功"}
@app.get('/heatch', response_model=HealthResponse)
async def heatch_cheack()-> HealthResponse:
    return HealthResponse(status="OK", message="Producet API is running")