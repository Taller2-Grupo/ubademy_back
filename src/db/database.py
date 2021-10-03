from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://szbbimktemtmxp:abb783d6b84c1f607061d64dacb901af10cae40d24a2b6d96110d7efe477b5c4@ec2-54-174-172-218.compute-1.amazonaws.com:5432/d3vhnlg19iblmb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
