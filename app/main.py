import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

from app.schemas.product import ProductResponse, ProductCreate

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

@app.post('/api/v1/products/preview', response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate) -> ProductResponse:
    now = datetime.datetime.now()
    new_product = ProductResponse(
        id=len(products) + 1,
        **product.model_dump(),
        created_at=now,
        updated_at=now
    )
    products.append(new_product)
    return new_product