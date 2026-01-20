from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from database import db

class Notas(db.Model):
    __tablename__ = "Notas"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    nota: Mapped[Text] = mapped_column(Text, nullable=False)


