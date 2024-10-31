from sqlalchemy import create_engine, MetaData
from databases import Database
from sqlalchemy.orm import sessionmaker

# String de conexion
DATABASE_URL = "mysql+aiomysql://root:p4$$w0rd@localhost:3306/jimbo"

database = Database(DATABASE_URL)
metadata = MetaData()

# instanciar engine y sesion
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush = false, bind = engine)
