from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class HealthResponse(BaseModel):
    status: str
    message: str
@app.get("/")
def root():
    return {"message": "FastAPI 项目启动成功"}
@app.get('/health', response_model=HealthResponse)
async def health_check()-> HealthResponse:
    return HealthResponse(status="ok", message="Product API is running")