from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field



class ProductBase(BaseModel):
    name:str = Field(min_length=1 ,max_length=100)
    description:str | None=None
    price:Decimal = Field(gt=0)
    stock:int = Field(ge=0)
    is_active:bool = Field(default=True)
class ProductCreate(ProductBase):
    pass
class ProductUpdate(BaseModel):
    name:str |None= Field(min_length=1 ,max_length=100)
    description:str | None=None
    price:Decimal |Field(default=None,gt=0)
    stock:int |None=Field(default=None,ge=0)
    is_active:bool | None=Field(default=None)
class ProductResponse(ProductBase):
    id:int =Field(gt=0)
    created_at:datetime
    updated_at:datetime
    model_config = ConfigDict(from_attributes=True)