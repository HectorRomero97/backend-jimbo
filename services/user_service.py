from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def create_user(self, user_name: str, email: str):
        return await self.repository.create_user(user_name, email)

    async def get_user_by_id(self, user_id: int):
        return await self.repository.get_user_by_id(user_id)

    async def get_users(self):
        return await self.repository.get_users()