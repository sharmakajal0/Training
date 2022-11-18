from typing import TYPE_CHECKING, List

import fastapi as _fastapi
from sqlalchemy.orm import Session

from app import schemas as _schemas
from app import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


app = _fastapi.FastAPI()

@app.post("/create-table/")
async def create_table(db: Session = _fastapi.Depends(_services.get_db)):
    _services._add_tables()

@app.post("/api/contacts/", response_model=_schemas.Contact)
async def create_contact(contact: _schemas.CreateContact, db: "Session" = _fastapi.Depends(_services.get_db)):
    return await _services.create_contact(contact=contact, db=db)

@app.get("/api/contacts/", response_model=List[_schemas.Contact])
async def get_contacts(db: "Session" = _fastapi.Depends(_services.get_db)):
    return await _services.get_contacts(db=db)

@app.get("/api/contacts/{contact_id}/", response_model=_schemas.Contact)
async def get_contact(user_id: int, db: "Session" = _fastapi.Depends(_services.get_db)):
    contact = await _services.get_contact_detail(contact_id=user_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="User not found")
    
    return contact

@app.delete("/api/contacts/{contact_id}/")
async def delete_contact(contact_id: int, db: "Session" = _fastapi.Depends(_services.get_db)):
    contact = await _services.get_contact_detail(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="User not found")
    
    contact_bool = await _services.delete_contact(contact=contact, db=db)
    if contact_bool:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_304_NOT_MODIFIED, detail="Contact not deleted")

    return {"Delete Status": "Success"}

@app.put("/api/contacts/{contact_id}/", response_model=_schemas.Contact)
async def update_contact(user_id: int, contact_data: _schemas.CreateContact, db: "Session" = _fastapi.Depends(_services.get_db)) -> _schemas.Contact:
    contact = await _services.get_contact_detail(contact_id=user_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="User not found")
    
    contact_bool = await _services.update_contact(contact_data=contact_data, contact=contact, db=db)
    if contact_bool is None:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_304_NOT_MODIFIED, detail="Contact not updated")
    
    return contact