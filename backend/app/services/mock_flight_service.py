from datetime import datetime, timezone

from app.models.flight import Flight, FlightResponse


def get_mock_flight_response() -> FlightResponse:
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
