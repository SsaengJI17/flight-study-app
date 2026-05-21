from fastapi import APIRouter

from app.models.flight import FlightResponse
from app.services.mock_flight_service import get_mock_flight_response


router = APIRouter(prefix="/api/flights", tags=["flights"])


@router.get("/mock", response_model=FlightResponse)
def get_mock_flights():
    return get_mock_flight_response()
