from pydantic import BaseModel, PositiveInt
from schemas.show_schemas import ShowOut


class OrderBase(BaseModel):
    amount: PositiveInt


class OrderIn(OrderBase):
    ...


class OrderOut(OrderBase):
    id: int
    amount: int
    show: ShowOut
