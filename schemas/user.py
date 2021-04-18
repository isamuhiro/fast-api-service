from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    address: str

    class Config:
        orm_mode = True


class UserResponse(UserSchema):
    id: int
