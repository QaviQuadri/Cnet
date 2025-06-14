from fastapi import FastAPI
from app.routes import crisis
from app.database import engine
from app import models
from app import models
from app.database import engine
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(crisis.router, prefix="/crisis", tags=["Crisis"])
