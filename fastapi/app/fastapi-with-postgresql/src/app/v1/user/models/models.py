import datetime as _dt
import sqlalchemy as _sql

from core.db.database import Base
class Contact(Base):
    __tablename__ = "contacts"

    id = _sql.Column(_sql.Integer, primary_key = True, index=True)
    firstname = _sql.Column(_sql.String, index=True)
    lastname = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True, unique=True)
    phone_number = _sql.Column(_sql.String, index=True, unique=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)