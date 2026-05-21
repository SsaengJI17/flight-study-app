# API Contract

## GET /health

Returns backend health status.

### Response

```json
{
  "status": "ok"
}
```

## GET /api/flights/mock

Returns mock flight data for Unity development.

### Response

```json
{
  "timestamp": "2026-05-21T12:00:00Z",
  "flights": [
    {
      "flight_id": "KE123",
      "airline_iata": "KE",
      "airline_icao": "KAL",
      "callsign": "KAL123",
      "latitude": 37.46,
      "longitude": 126.44,
      "altitude_m": 1200,
      "true_track": 270,
      "ground_speed": 145,
      "departure_airport": "ICN",
      "arrival_airport": "NRT",
      "estimated_remaining_minutes": 95
    }
  ]
}
```
