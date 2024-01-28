from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text

from connection import engine


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    title_type = Column(String)
    description = Column(String)


class MoneyMovement(Base):
    __tablename__ = "money_movement"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    action = Column(String)
    category_id = Column(ForeignKey("category.id"))
    category_id_source = Column(ForeignKey("category.id"))
    last_balance = Column(Integer)
    amount = Column(Integer)
    description = Column(String)
