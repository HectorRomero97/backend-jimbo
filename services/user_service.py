from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import UserRepository
from sqlalchemy.exc import IntegrityError
from models.user_model import User

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(db)

    async def create_user(self, user_name: str, email: str):
        user = User(user_name=user_name, email = email)
        try:
            return await self.repository.create_user(user_name, email)
        except IntegrityError:
            await self.db.rollback()
            return {"error": "A user with this email already exists"}

    async def get_user_by_id(self, user_id: int):
        return await self.repository.get_user_by_id(user_id)

    async def get_users(self):
        return await self.repository.get_users()
  