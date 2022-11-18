from typing import TYPE_CHECKING, List

from fastapi import Depends
import core.db.database as _database
from ..models import models as _models
from ..schemas import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

async def create_contact(contact: _schemas.CreateContact, db: "Session" = Depends(get_db())) -> _schemas.Contact:
    contact = _models.Contact(**contact.dict())
    db.add(contact) 
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.from_orm(contact)

async def get_contacts(db: "Session" = Depends(get_db())) -> List[_schemas.Contact]:
    contacts = db.query(_models.Contact).all()
    return list(map(_schemas.Contact.from_orm, contacts))

async def get_contact_detail(contact_id: int, db: "Session" = Depends(get_db())) -> List[_schemas.Contact]:
    contact = db.query(_models.Contact).filter(_models.Contact.id == contact_id).first()
    return contact

async def delete_contact(contact: _models.Contact, db: "Session" = Depends(get_db())):
    db.delete(contact)
    db.commit()

async def update_contact(contact_data: _schemas.CreateContact, contact: _models.Contact, db: "Session" = Depends(get_db)) -> _schemas.Contact:
    contact.firstname = contact_data.firstname
    contact.lastname = contact_data.lastname
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number

    db.commit()
    db.refresh(contact)

    return _schemas.Contact.from_orm(contact)