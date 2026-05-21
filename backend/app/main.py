from fastapi import FastAPI

from app.routers.flights import router as flights_router


app = FastAPI(title="Flight Study App Backend")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(flights_router)
