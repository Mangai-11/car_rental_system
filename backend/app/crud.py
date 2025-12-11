from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# -----------------------------
# CAR CRUD FUNCTIONS
# -----------------------------

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(
        make=car.make,
        model=car.model,
        year=car.year,
        daily_rate=car.daily_rate,
        available=True
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_cars(db: Session):
    return db.query(models.Car).all()

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

# -----------------------------
# RENTAL CRUD FUNCTIONS
# -----------------------------

def create_rental(db: Session, car_id: int, rent: schemas.RentRequest):
    car = get_car(db, car_id)
    if not car:
        raise ValueError("Car not found")

    if not car.available:
        raise ValueError("Car is not available")

    # Create rental
    rental = models.Rental(
        car_id=car_id,
        user_name=rent.user_name,
        start_date=rent.start_date,
        end_date=rent.end_date,
        rental_date=datetime.utcnow()
    )

    car.available = False # Mark car unavailable

    db.add(rental)
    db.commit()
    db.refresh(rental)

    return rental

def cancel_rental(db: Session, rental_id: int):
    rental = db.query(models.Rental).filter(models.Rental.id == rental_id).first()
    if not rental:
        return False

    car = get_car(db, rental.car_id)
    car.available = True # Make the car available again

    db.delete(rental)
    db.commit()

    return True



def get_rental_by_car(db: Session, car_id: int):
    return db.query(models.Rental).filter(models.Rental.car_id == car_id).first()