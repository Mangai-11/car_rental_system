Car Rental System — Full Stack Project

Using FastAPI + SQLite + ReactJS + OpenAPI Python SDK


---

🚀 Project Overview

This project implements a Car Rental System with:

FastAPI backend

SQLite database

React frontend

Auto-generated Python SDK (OpenAPI Generator CLI)

Batch files for automated setup



---

🛠️ Setup Instructions


---

1️⃣ Backend Setup

Requirements

Python 3.14.2

pip

Virtual environment support



---

Steps

1. Navigate to backend folder

cd backend

2. Create & activate virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

3. Install backend dependencies

pip install -r requirements.txt

4. Run the FastAPI server

uvicorn app.main:app --reload

Backend will start at:

➡ http://127.0.0.1:8000
➡ Swagger UI: http://127.0.0.1:8000/docs


---

2️⃣ Frontend Setup (ReactJS)

Requirements

Node.js + npm installed



---

Steps

1. Navigate to frontend folder

cd frontend

2. Install dependencies

npm install

3. Start frontend

npm start

Frontend runs at:

➡ http://localhost:3000


---

3️⃣ SDK Generation (Python)

This project uses OpenAPI Generator CLI.

Run the following command from backend folder:

npx @openapitools/openapi-generator-cli generate -i http://127.0.0.1:8000/openapi.json -g python -o sdk

This will generate the /sdk folder.


---

4️⃣ Automation Scripts

run_backend.bat

cd backend
uvicorn app.main:app --reload

run_frontend.bat

cd frontend
npm start


---

✔️ Features Implemented

Add new cars

List all cars

View car details

Rent a car

Cancel a rental

View rental history

React frontend integrated

SDK auto-generated



---

📦 Project Structure

car_rental_system/

├── backend/

  │ ├── app/

    │ │ ├── main.py
    │ │ ├── models.py
    │ │ ├── crud.py
    │ │ ├── schemas.py
    │ │ ├── database.py
    │ ├── car_rental.db
    
│ ├── requirements.txt

│ └── README.md 

│
├── frontend/
 
    │ ├── src/
     
       │ │ ├── pages/
         │ │ ├── ListCars.js
         │ │ │ ├── CarDetails.js
         │ │ │ ├── RentCar.js
         │ │ │ ├── RentalPage.js
         │ │ ├── App.js
         │ │ ├── index.js
│ ├── package.json

│ ├── public/

│ └── README.md (auto-created by React)

│
├── sdk/

    │ └── (Auto-generated Python SDK files)
    
│
├── run_backend.bat

├── run_frontend.bat

└── README.md


