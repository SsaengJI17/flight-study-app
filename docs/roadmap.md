# Development Roadmap

## Phase 0: Project Setup

- Create repository structure
- Configure GitHub
- Add project rules
- Add documentation skeleton

## Phase 1: Backend MVP

- Create FastAPI app
- Add `/health`
- Add `/api/flights/mock`
- Define Pydantic response models
- Add backend tests
- Document API response schema

## Phase 2: Unity MVP

- Create Unity project
- Add placeholder aircraft object
- Fetch mock flight API
- Convert latitude/longitude/altitude to Unity coordinates
- Smooth aircraft movement with interpolation

## Phase 3: Real Flight Data

- Add AeroDataBox client
- Add OpenSky client
- Add airline IATA to ICAO mapping
- Match scheduled flights with live aircraft positions
- Add caching and fallback behavior

## Phase 4: Study UX

- Add cabin camera view
- Add Pomodoro timer
- Add remaining flight time display
- Add cabin ambient sound
- Add local study session storage

## Phase 5: Assets and Polish

- Create cabin seat/window models in Blender
- Add aircraft models
- Add airline-inspired materials
- Add airport lounge menu scene

## Phase 6: Deployment

- Deploy FastAPI backend to Oracle Cloud
- Add systemd or Docker setup
- Monitor resource usage
