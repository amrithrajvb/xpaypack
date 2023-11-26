from fastapi import APIRouter,HTTPException,Path,Depends,UploadFile,File

import crud
from models import UserProfile
from connection import SessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema,RequestUser,Response

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create(request:UserSchema,db:Session=Depends(get_db)):
    print("parameterss",request.UserId,request.email,request.username,request.phone,request.hashed_password)
    # image=profile_picture.file.read()
    # db_profile = UserProfile(UserId=request.UserId, image=profile_picture.file.read())
    # db.add(db_profile)
    # db.commit()
    crud.Create_User(db,request)
    return {"message": "User registered successfully"}


@router.get("/allusers")
async def get(db:Session=Depends(get_db), _user=None):
    _user=crud.get_user(db,0,100)
    return _user
@router.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _users=crud.get_user_by_id(db,id)
    return _users
