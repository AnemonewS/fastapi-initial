import time

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from db import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@router.get('/')
async def get_operations(
    operation_type: str,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(operation).where(operation.c.type == operation_type)
    response = await session.execute(query)
    return response


@router.post('/')
async def create_operation(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(operation).values(
        **new_operation.dict()
    )
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}


@router.get('/long_operation')
@cache(expire=30)
async def get_long_page():
    time.sleep(2)
    return 'Очень долгая операция!'
