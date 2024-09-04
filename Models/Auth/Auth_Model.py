from pydantic import BaseModel



# Auth model

class Auth(BaseModel):
    email:str