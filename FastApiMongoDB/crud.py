from sqlalchemy.orm import Session
from models import UserDB,UserProfile
from schemas import UserSchema
from fastapi import FastAPI, HTTPException,File,UploadFile
from secrets import token_hex
from config import mongo_collection
#all Users
def get_user(db:Session,skip:int=0,limit:int=100):
    return db.query(UserDB).offset(skip).limit(limit).all()
#get by UserId
def get_user_by_id(db:Session,UserId:int):
    return db.query(UserDB).filter(UserDB.UserId==str(UserId)).first()

#create User
def Create_User(db:Session,user:UserSchema,profile:UploadFile=File(...)):

    #Note We need Profile Picture-so need to add file: UploadFile = File(...) as argument. When i am trying this getting  some
    # encoding related issue.Eventhough i have put the query below for inserting the data into db
    _user = db.query(UserDB).filter(UserDB.email == user.email).first()
    if _user:
        raise HTTPException(status_code=400, detail="Email already exists")
    _user = db.query(UserDB).filter(UserDB.UserId == user.UserId).first()
    if _user:
        raise HTTPException(status_code=400, detail="User already exists!")

    _user=UserDB(UserId=user.UserId,username=user.username,email=user.email,phone=user.phone,hashed_password=user.hashed_password)
    db.add(_user)
    db.commit()

    #####Profile Picture ####

    if profile:
        profile_data = {"user_id": str(_user.user_id), "profile_picture": profile.file.read()}
        mongo_collection.insert_one(profile_data)
    db.add(_user)
    db.commit()
    # return {"message": "User registered successfully"}
    db.refresh(_user)
    return {"message": "User registered successfully","user":_user}







#
# def remove_user(db:Session,User_id:int):
#     _user=get_user_by_id(db=db,UserId=User_id)
#     db.delete(_user)
#     db.commit()
#
# def update_user(db:Session,User_id:int,username:str,email:str,phone:int,password:str):
#     _user=get_user_by_id(db=db,User_id=User_id)
#     _user.username=username
#     _user.email=email
#     _user.phone=phone
#     _user.hashed_password=password

