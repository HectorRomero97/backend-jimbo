import sqlalchemy
from ..repositories import user_repository

async def get_users():
    users = await user_repository.get_users()
    return users

async def get_user(user_id: int):
    user = await user_repository.get_user(user_id)
    return user

async def update_user(user_id: int):
    return 1

async def delete_user_by_id(user_id: int):
    return 1