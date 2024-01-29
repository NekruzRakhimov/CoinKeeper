# from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
# from sqlalchemy.orm import DeclarativeBase, relationship
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     surname = Column(String)
#     age = Column(Integer)
#     is_deleted = Column(Boolean, default=False)
#     account = relationship("Account", back_populates="user")
#
#
# class Account(Base):
#     __tablename__ = 'accounts'
#     account_number = Column(Integer, primary_key=True, index=True)
#     balance = Column(Integer, default=0)
#     is_deleted = Column(Boolean, default=False)
#     user = relationship("User", back_populates="account")
#     user_id = Column(Integer, ForeignKey("users.id"))


# -----------------------------------------------------------------------------------------------------------------------

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class ExpensesCategories(Base):
    __tablename__ = 'expenses_categories'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    unique_title = Column(String, unique=True)


class Balances(Base):
    __tablename__ = 'balances'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    balance = Column(DECIMAL(10, 1), default=0.0)
    unique_title_balance = Column(String, unique=True)


class Expenses(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('expenses_categories.id'))
    amount = Column(DECIMAL(10, 1))
    balance_id = Column(Integer, ForeignKey('balances.id'))
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')


class Incomes(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(DECIMAL(10, 1))
    unique_title_amount = Column(String, unique=True)

