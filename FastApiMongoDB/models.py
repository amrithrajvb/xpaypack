from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# from .database import Base
from connection import Base,SQLALCHEMY_DATABASE_URL
from sqlalchemy import create_engine, Column, Integer, String, Boolean,LargeBinary

class UserDB(Base):
    __tablename__ = "Authuser"

    id = Column(Integer, primary_key=True, index=True)
    UserId = Column(String,index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(Integer, index=True)
    hashed_password = Column(String)
    # profile_picture=Column(,index=True)
    is_active = Column(Boolean, default=True)

#
class UserProfile(Base):
    __tablename__ = "userprofiles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # UserId = Column(String, ForeignKey("users.UserId"))
    UserId=Column(String,index=True)
    images = Column(LargeBinary)







