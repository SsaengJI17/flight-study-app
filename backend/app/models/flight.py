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
