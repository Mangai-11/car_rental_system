from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import SessionLocal
from . import crud, models, schemas

# Create the FastAPI app
app = FastAPI(title="Car Rental System")

# ---------------------------
# CORS Middleware (Required)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins (React frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Database Dependency
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# CAR ENDPOINTS
# ---------------------------

@app.post("/cars/", response_model=schemas.CarOut)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)

@app.get("/cars/", response_model=list[schemas.CarOut])
def list_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db)

@app.get("/cars/{car_id}", response_model=schemas.CarOut)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.get_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

# ---------------------------
# RENTAL ENDPOINTS
# ---------------------------

@app.post("/cars/{car_id}/rent", response_model=schemas.RentalOut)
def rent_car(car_id: int, rent: schemas.RentRequest, db: Session = Depends(get_db)):
    try:
        rental = crud.create_rental(db, car_id, rent)
        return rental
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/rentals/{rental_id}")
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    success = crud.cancel_rental(db, rental_id)
    if not success:
        raise HTTPException(status_code=404, detail="Rental not found")
    return {"detail": "Rental cancelled successfully"}

@app.get("/rentals/car/{car_id}", response_model=schemas.RentalOut)
def get_rental_for_car(car_id: int, db: Session = Depends(get_db)):
    rental = crud.get_rental_by_car(db, car_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental