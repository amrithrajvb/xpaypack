from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
# from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL ="postgresql://postgres:Password123@localhost:5432/fastxpay"
database = Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,encoding="utf-8"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# async def startup_db_client():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown_db_client():
#     await database.disconnect()

