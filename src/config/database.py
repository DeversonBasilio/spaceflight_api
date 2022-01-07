import sqlalchemy as _sql
from sqlalchemy.engine import create_engine
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.sql.expression import false

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://ifa5jh31yxnmydus:klitwc7ub1m0hvh6@l6glqt8gsx37y4hs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/r1spg75hiiwyd8uq"

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = _declarative.declarative_base()
