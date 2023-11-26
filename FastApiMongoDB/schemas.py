from typing import List,Optional,Generic,TypeVar
# from pydantic.generics import
from typing import Optional
from pydantic import BaseModel, Field

T= TypeVar('T')

class UserSchema(BaseModel):
    UserId: str
    username: str
    email: str
    phone: str
    hashed_password: str


    class Config:
        from_orm = True

class RequestUser(BaseModel):
    parameter: UserSchema = Field(..., description="User data in the request body")





#
# class UserSchema(BaseModel):
#     id: Optional[int]=None
#     UserId=Optional[int]=None
#     username: Optional[str]=None
#     email:Optional[str]=None
#     password:Optional[str]=None
#     phone: Optional[int]=None
#
#     class Config:
#         from_attributes = True
#
#
# class RequestUser(BaseModel):
#     parameter: UserSchema = Field(..., description="User data in the request body")
# class RequestUser(BaseModel):
#     parameter: UserSchema=Field(...)
#
# from pydantic import BaseModel, Field
#
# class UserSchema(BaseModel):
#     UserId:str
#     username: str
#     email: str
#     phone: str
#     password: str
#
#
#     class Config:
#         from_attributes = True

# class RequestUser(BaseModel):
#     parameter: UserSchema = Field(..., description="User data in the request body")



class Response(BaseModel,Generic[T]):
    code:str
    status:str
    message:str
    result:Optional[T]

