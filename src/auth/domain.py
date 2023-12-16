from pydantic import BaseModel, EmailStr, Field, ConfigDict


class AuthBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    password: str = Field(..., min_length=3, max_length=256) # TODO change min pass length


class Signup(AuthBase):
    first_name: str = Field(..., min_length=2, max_length=30)
    last_name: str = Field(..., min_length=2, max_length=30)


class Login(AuthBase):
    ...


class AccessToken(BaseModel):
    access_token: str
    token_type: str = "Bearer"
