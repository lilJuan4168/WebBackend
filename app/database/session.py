from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session 
from app.core.config import settings

#DATABASE_URL = ("postgresql+psycopg://manuel:lol4168@localhost:5432/tienda_de_electronica")

#engine = create_engine(settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()