import asyncio
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from database import async_engine, AsyncSessionLocal, Base
from services.user_service import UserService

app = FastAPI()

# Obtener Sesion
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# Creacion de Tablas
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/users/")
async def create_user(name: str, email: str, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    return await user_service.create_user(name, email)

@app.get("/users/{user_id}")
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    user = await user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    users = await user_service.get_users()
    return users