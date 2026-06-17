from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field



class ProductBase(BaseModel):
    id: int = Field(gt=0)
    name:str = Field(min_length=1 ,max_length=100)
    description:str | None
    price:Decimal = Field(gt=0)
    stock:int = Field(ge=0)
    is_active:bool = Field(default=True)
class ProductCreate(ProductBase):
    pass
class ProductUpdate(ProductBase):
    name:str = Field(default=None,min_length=1 ,max_length=100)
    description:str | None=None
    price:Decimal |Field(default=None,gt=0)
    stock:int |Field(default=None,ge=0)
    is_active:bool | Field(default=None)
class ProductResponse(ProductBase):
    created_at:datetime
    updated_at:datetime

model_config = ConfigDict(from_attributes=True)