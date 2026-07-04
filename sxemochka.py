from sqlalchemy.orm import Mapped, mapped_column
from db import Base, engine, SessionLocal
class Game(Base):
    __tablename__ = 'games'
    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    price:Mapped[int]