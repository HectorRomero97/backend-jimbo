Requisitos:
pip install fastapi

pip install uvicorn

pip install sqlalchemy

pip install databases

pip install pymysql

pip install asyncpg

Solo necesita que exista una base de datos con el nombre jimbo (o cambiar el nombre de la base de datos que esta al final del string de conexion y configurar la variable:

DATABASE_URL = "mysql+aiomysql://usuario:contraseña@localhost:3306/jimbo"

esta variable esta dentro de Database.py

Ejecucion:

uvicorn main:app --reload;
