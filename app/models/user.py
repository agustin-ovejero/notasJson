from ..extensions import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Usuario(db.Model):
    __tablename__ = "Usuario"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(length=50), nullable=False)
    email: Mapped[str] = mapped_column(String(length=250), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(length=250), nullable=False) # El hash_password se creara en su función correspondiente
    