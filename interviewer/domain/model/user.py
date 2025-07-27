from pydantic import BaseModel


class User(BaseModel):
    class Config:
        from_attributes = True

    name: str
    did: str
    avatar: str
    createdAt: str
    updatedAt: str
    signature: str


class UserState(BaseModel):
    class Config:
        from_attributes = True

    owner: str
    did: str
    status: str
    role: str
    createdAt: str
    updatedAt: str
    signature: str