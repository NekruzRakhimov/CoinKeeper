from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text

from connection import engine


class Base(DeclarativeBase):
    pass


class ExpensesCategories(Base):
    __tablename__ = "expenses_categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Numeric(10, 2))
    balance_id = Column(ForeignKey("balances.id"))
    balance = relationship("Balances", backref="incomes")


class Balances(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    balance = Column(Numeric(10, 2))
    incomes = relationship("Incomes", backref="balance")


class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    category_id = Column(ForeignKey("expenses_categories.id"))
    amount = Column(Numeric(10, 2))
    balance_id = Column(ForeignKey("balances.id"))
    created_at = Column(DateTime)
    category = relationship("ExpensesCategories", backref="expenses")
    balance = relationship("Balances", backref="expenses")


Base.metadata.create_all(bind=engine)
