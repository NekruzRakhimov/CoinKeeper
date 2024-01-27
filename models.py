from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text

# from connection import engine


class Base(DeclarativeBase):
    pass
