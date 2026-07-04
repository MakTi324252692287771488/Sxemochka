from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from foxtrot import DB_URL
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass