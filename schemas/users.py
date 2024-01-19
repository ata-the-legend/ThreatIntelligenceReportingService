from pydantic import BaseModel

class BaseUser(BaseModel):
    name:str
    email: str
    
class CreateUser(BaseUser):
    password: str

class ReadUser(BaseUser):
    id: int
    
    class config:
        orm_mode = True

class ListUser(BaseUser):
    class config:
        orm_mode = True


