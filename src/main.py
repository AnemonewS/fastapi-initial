from __future__ import annotations

import aioredis
from fastapi import FastAPI

from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.operations.router import router as operation_router
from src.tasks.router import router as task_router

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(operation_router)
app.include_router(task_router)


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url(
        'redis://localhost',
        encoding='utf8',
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
