from pydantic import BaseModel

class UserCreated(BaseModel):
    name: str
    username: str
    email: str
    password: str
