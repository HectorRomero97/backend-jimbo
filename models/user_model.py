from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer,primary_key = True,  index = True, autoincrement = True)
    user_name = Column(String(255), nullable = False)
    email = Column(String(255), unique = True, nullable = False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")