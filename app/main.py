from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import Station
from app.schemas import Status, StationCreate, StationRead, StationUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/stations", response_model=StationRead, status_code=201)
def create_station(data: StationCreate, db: Session = Depends(get_db)):
    station = Station(**data.model_dump())
    db.add(station)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Ce code est déjà utilisé")
    db.refresh(station)
    return station

@app.get("/stations", response_model=list[StationRead])
def list_stations(status: Status | None = None, db: Session = Depends(get_db)):
    query = select(Station)
    if status is not None:
        query = query.where(Station.status == status)
    return db.scalars(query).all()

@app.get("/stations/{station_id}", response_model=StationRead)
def get_station(station_id: int, db: Session = Depends(get_db)):
    station = db.get(Station, station_id)
    if station is None:
        raise HTTPException(status_code=404, detail="Station introuvable")
    return station

@app.patch("/stations/{station_id}", response_model=StationRead)
def update_station(station_id: int, data: StationUpdate, db: Session = Depends(get_db)):
    station = db.get(Station, station_id)
    if station is None:
        raise HTTPException(status_code=404, detail="Station introuvable")
    for field, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(station, field, value)
    db.commit()
    db.refresh(station)
    return station