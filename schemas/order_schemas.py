from pydantic import BaseModel, PositiveInt


class OrderBase(BaseModel):
    amount: PositiveInt


class OrderIn(OrderBase):
    ...
