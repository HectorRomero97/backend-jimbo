import asyncio
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from database import async_engine, AsyncSessionLocal, Base
from services.user_service import UserService
from services.product_service import ProductService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

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

#Rutas Usuarios

@app.post("/users/")
async def create_user(user_name: str, email: str, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    return await user_service.create_user(user_name, email)

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

#Rutas Productos

@app.post("/products/")
async def create_product(product_name: str, price: float ,product_description: str = None ,db: AsyncSession = Depends(get_db)):
    product_service = ProductService(db)
    return await product_service.create_product(product_name, price, product_description)

@app.get("/products/{product_id}")
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product_service = ProductService(db)
    product = await product_service.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="User not found")
    return product

@app.get("/products/")
async def read_products(db: AsyncSession = Depends(get_db)):
    product_service = ProductService(db)
    products = await product_service.get_products()
    return products