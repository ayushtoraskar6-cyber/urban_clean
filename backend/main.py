from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import math
import requests

import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="UrbanClean API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- AUTH ENDPOINTS ---
@app.post("/api/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Extract user data into a dict and pop the raw password
    user_data = user.dict()
    raw_password = user_data.pop("password")
    
    # Store plain or hashed password into password_hash
    # (For production/demo: models.User expects password_hash)
    new_user = models.User(**user_data, password_hash=raw_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# --- CITIZEN ENDPOINTS ---
@app.post("/api/complaints")
def create_complaint(complaint: schemas.ComplaintCreate, db: Session = Depends(get_db)):
    new_complaint = models.Complaint(**complaint.dict())
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    return new_complaint

# --- DRIVER ROUTE OPTIMIZATION (TSP + OSRM) ---
@app.get("/api/driver/optimize-route")
def optimize_route(lat: float, lng: float, city: str, db: Session = Depends(get_db)):
    pending = db.query(models.Complaint).filter(
        models.Complaint.city == city, 
        models.Complaint.status == "Pending"
    ).all()

    if not pending:
        return {"stops": [], "osrm_route": None}

    # Nearest Neighbor TSP calculation
    current_pos = (lat, lng)
    unvisited = list(pending)
    ordered_stops = []

    while unvisited:
        nearest = min(
            unvisited, 
            key=lambda c: math.hypot(c.latitude - current_pos[0], c.longitude - current_pos[1])
        )
        ordered_stops.append(nearest)
        current_pos = (nearest.latitude, nearest.longitude)
        unvisited.remove(nearest)

    # Fetch geometry from OSRM
    coords_str = f"{lng},{lat};" + ";".join([f"{s.longitude},{s.latitude}" for s in ordered_stops])
    osrm_url = f"http://router.project-osrm.org/route/v1/driving/{coords_str}?overview=full&geometries=geojson"
    osrm_res = requests.get(osrm_url).json()

    return {
        "stops": ordered_stops,
        "coordinates": osrm_res["routes"][0]["geometry"]["coordinates"],
        "distance_km": round(osrm_res["routes"][0]["distance"] / 1000, 2),
        "duration_mins": round(osrm_res["routes"][0]["duration"] / 60)
    }

# --- ADMIN METRICS ---
@app.get("/api/admin/dashboard")
def admin_dashboard(state: str, district: str, city: str, db: Session = Depends(get_db)):
    complaints = db.query(models.Complaint).filter(
        models.Complaint.state == state,
        models.Complaint.district == district,
        models.Complaint.city == city
    ).all()

    total_today = db.query(models.Complaint).count()
    solved_today = db.query(models.Complaint).filter(models.Complaint.status == "Completed").count()
    drivers = db.query(models.User).filter(models.User.role == "driver").all()

    return {
        "complaints": complaints,
        "metrics": {"totalToday": total_today, "solvedToday": solved_today},
        "onDutyDrivers": drivers
    }