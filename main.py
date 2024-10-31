from fastapi import FastAPI
from .models import users
from .database import database
from .services import user_service
from .repositories import user_repository

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.get("/users/")
async def root():
    users = await user_service.get_users()
    if users is None:
        raise HTTPException(status_code = 404, detail="Users not found")
    return users;    

@app.get("/users/{user_id}")
async def read_user():
    user = await user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user;

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()