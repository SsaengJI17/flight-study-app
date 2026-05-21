# AGENTS.md

## Project Goal

Build a real-time 3D virtual flight study app.

The app combines:
- Real-time flight data
- A Unity 3D cabin/aircraft experience
- Study tools such as Pomodoro timer, remaining flight time, and ambient cabin sound
- Python FastAPI backend
- Oracle Cloud deployment
- Blender-created 3D assets

## Repository Structure

- `backend/` : Python FastAPI backend
- `unity/` : Unity client project
- `blender/` : Blender source assets
- `docs/` : project documentation
- `.github/` : GitHub workflows and templates

## General Rules

- Read this file before making changes.
- Do not modify files outside the requested scope.
- Prefer small, focused changes.
- Do not rewrite working code unless necessary.
- Do not commit API keys, tokens, passwords, `.env` files, Unity `Library/`, or build outputs.
- Keep API responses documented in `docs/api-contract.md`.
- Update documentation when behavior changes.
- Add tests for backend logic when possible.

## Backend Rules

- Use FastAPI.
- Use Pydantic models for request and response schemas.
- Keep external API integrations isolated under `backend/app/services/`.
- Keep Unity-facing API responses stable.
- If external flight APIs fail, the backend should return cached or mock data instead of crashing.

## Unity Rules

- Keep runtime scripts under `Assets/Scripts/`.
- Do not hardcode production API keys.
- Do not hardcode server URLs directly in gameplay scripts.
- Use configuration files, ScriptableObjects, or environment-specific settings.
- Keep placeholder assets simple until the data pipeline is working.

## Blender Rules

- Keep source `.blend` files under `blender/`.
- Export Unity-ready assets separately.
- Prefer lightweight assets suitable for mobile/tablet performance.

## Commit Style

Use clear commit messages:

- `chore:`
- `feat:`
- `fix:`
- `docs:`
- `refactor:`
- `test:`

Examples:
- `feat: add mock flight API`
- `docs: update API contract`
- `fix: handle empty flight response`
