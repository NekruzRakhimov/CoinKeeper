from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric


class Base(DeclarativeBase):
    pass


class ExpensesCategory(Base):
    __tablename__ = "expenses_categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)


class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    category_id = Column(ForeignKey("expenses_categories.id"))
    amount = Column(Numeric(20, 2))
    balance_id = Column(ForeignKey("balances.id"))
    created_at = Column(DateTime)


class Balances(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    balance = Column(Numeric(20, 2))


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Numeric(20, 2))
