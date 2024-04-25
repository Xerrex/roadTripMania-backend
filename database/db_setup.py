from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import CONFIG as CF


SQLALCHEMY_DATABASE_URL = CF.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=CF.DATABASE_CONNECT_ARGS)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
