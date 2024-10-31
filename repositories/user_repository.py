from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user_model import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_user(self, user_name: str, email: str):
        user = User(user_name=user_name, email=email)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return user

    async def get_users(self):
        query = select(User)
        result = await self.db.execute(query)
        return result.scalars().all()  

    async def get_user_by_id(self, user_id: int):
        query = select(User).where(User.user_id == user_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()