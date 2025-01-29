from fastapi import FastAPI
from api.endpoints import router

app = FastAPI()

# Include the endpoints for the rental-related data
app.include_router(router)
