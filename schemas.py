from pydantic import BaseModel, Field

class UserBase(BaseModel):
    fio: str = Field(default=..., description="User Name")

class UserCreate(UserBase):
    id: int = Field(default=..., description="User ID")

class UserRead(UserBase):
    id: int
    class Config:
        orm_mode=True
