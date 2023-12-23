from fastapi import APIRouter

from ..models.sensor_models import SensorData, SensorDataIn

router = APIRouter()

sensor_data_table = {}


@router.post("/sensor-data", response_model=SensorData, status_code=201)
async def post_sensor_data(sensor_data: SensorDataIn):
    data = sensor_data.model_dump()
    last_record_id = len(sensor_data_table)
    new_record = {**data, "id": last_record_id}
    sensor_data_table[last_record_id] = new_record
    return new_record


@router.get("/sensor-data", response_model=list[SensorData])
async def get_all_sensor_data():
    return list(sensor_data_table.values())
