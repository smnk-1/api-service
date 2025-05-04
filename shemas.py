from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(default=..., description="User ID")
    fio: str = Field(default=..., description="User Name")

class UserCreate(User):
    pass

class UserRead(User):
    pass
