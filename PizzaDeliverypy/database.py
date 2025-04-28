from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/postgres'

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)