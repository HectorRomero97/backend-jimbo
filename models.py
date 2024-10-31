from sqlalchemy import Table, Column, Integer, String, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func
from .database import metadata


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key = True, autoincrement = True),
    Column("name", String(255), nullable = False),
    Column("email", String(255), unique = True, nullable = False),
    Column("created_at", TIMESTAMP, server_default=func.now())
)

products = Table(
    "products",
    metadata,
    Column("product_id", Integer, primary_key=true),
    Column("product_name", String(255) ),
    Column("product_description",String(255), nullable=True, ),
    Column("Price", DECIMAL(10,2), nullable=False),
    Column("created_at", TIMESTAMP, server_default=func.now())
)