from pydantic import BaseModel
from pydantic import EmailStr
class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserOut(BaseModel):
    username: str
    password: str
    email: EmailStr

    class Config:
        orm_mode = True
