from fastapi import FastAPI

from .routers.sensor_routes import router as sensor_data_router


app = FastAPI()
app.include_router(sensor_data_router)
