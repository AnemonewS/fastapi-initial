import pytz

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP
from datetime import datetime

from db import metadata

timezone = pytz.timezone('Europe/Moscow')
current_date = datetime.now(tz=timezone)

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("type", String),
    Column("date", TIMESTAMP),
)
