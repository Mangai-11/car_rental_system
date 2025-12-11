from pydantic import BaseModel

from datetime import datetime

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    daily_rate: float

class CarOut(CarCreate):
    id: int
    available: bool

    class Config:
        orm_mode = True


class RentRequest(BaseModel):
    user_name: str
    start_date: datetime
    end_date: datetime


class RentalOut(BaseModel):
    id: int
    car_id: int
    user_name: str
    start_date: datetime
    end_date: datetime
    rental_date: datetime

    class Config:
        orm_mode = True