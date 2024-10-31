from sqlalchemy import select
from ..models.user import User
from ..database import database

async def get_users():
    query = select(users)
    return database.fetch_all(query)

async def get_user_by_id(user_id: int):
    query = select(users).where(users.c.user_id == user_id)
    return await database.fetch_one(query)

