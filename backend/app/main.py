from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel


class Flight(BaseModel):
    flight_id: str
    airline_iata: str
    airline_icao: str
    callsign: str
    latitude: float
    longitude: float
    altitude_m: int
    true_track: float
    ground_speed: float
    departure_airport: str
    arrival_airport: str
    estimated_remaining_minutes: int


class FlightResponse(BaseModel):
    timestamp: str
    flights: list[Flight]


app = FastAPI(title="Flight Study App Backend")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/flights/mock", response_model=FlightResponse)
def get_mock_flights():
    return FlightResponse(
        timestamp=datetime.now(timezone.utc).isoformat(),
        flights=[
            Flight(
                flight_id="KE123",
                airline_iata="KE",
                airline_icao="KAL",
                callsign="KAL123",
                latitude=37.46,
                longitude=126.44,
                altitude_m=1200,
                true_track=270,
                ground_speed=145,
                departure_airport="ICN",
                arrival_airport="NRT",
                estimated_remaining_minutes=95,
            )
        ],
    )
