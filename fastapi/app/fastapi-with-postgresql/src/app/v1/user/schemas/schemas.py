import datetime as _dt
from pydantic import BaseModel

class _BaseContact(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone_number: str

class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True

class CreateContact(_BaseContact):
    pass