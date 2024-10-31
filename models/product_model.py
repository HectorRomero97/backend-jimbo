from sqlalchemy import  Column, Integer, String, DECIMAL, TIMESTAMP
from database import Base
from sqlalchemy.sql import func


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer,primary_key = True,  index = True, autoincrement = True)
    product_name = Column(String(255), nullable = False)
    product_description = Column(String(255), nullable = True)
    price = Column(DECIMAL(10,2), nullable = False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable = False)
