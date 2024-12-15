from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        orm_mode = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user: UserResponse
    class Config:
        orm_mode = True
