from fastapi import FastAPI

from database.db_setup import engine
from database import models


models.Base.metadata.create_all(bind=engine)

title = "Road Trip Mania Backend"
description = "Backend for the road trip mania app"
version = "1.0"
prefix = f"/api/v{version}"

app = FastAPI(title=title, description=description, version=version)

@app.get("/")
def home():
    return {"msg": "Welcome to RoadTripMania Backend."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")