import pytz

from pydantic import BaseModel
from datetime import datetime

timezone = pytz.timezone('Europe/Moscow')
current_date = datetime.now(tz=timezone)


class OperationCreate(BaseModel):
    quantity: str
    type: str
