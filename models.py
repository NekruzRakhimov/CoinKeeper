'''from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text

from connection import engine



class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    type_of_title = Column(String)
    description = Column(String)

class MoneyMovement(Base):
    __tablename__ = "money_movement"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    action = Column(String)
    category_id = Column(ForeignKey("category.id"))
    category_id_source = Column(ForeignKey("category.id"))
    last_balance = Column(Integer, default=1000)
    amount = Column(Integer)
    description = Column(String)

class Balances(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    balance = Column(Integer, default=100)

class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True)
    category_id = Column(ForeignKey("categories.id"))
    category_id_source = Column(ForeignKey("categories.id"))
    balance_id = Column(ForeignKey("balances.id"))
    amount = Column(Integer)
    created_at = Column(DateTime)


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    amount = Column(Integer)
'''
'''
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text

from connection import engine


class Base(DeclarativeBase):
    pass


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    title_type = Column(String)
    description = Column(String)


class Balances(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    balance = Column(Integer, default=100)


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
'''

from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text

from connection import engine


class Base(DeclarativeBase):
    pass


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    title_type = Column(String)
    description = Column(String)


class Balances(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    balance = Column(Integer, default=100)

'''
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
'''

class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True)
    category_id = Column(ForeignKey("categories.id"))
    category_id_source = Column(ForeignKey("categories.id"))
    balance_id = Column(ForeignKey("balances.id"))
    amount = Column(Integer)
    created_at = Column(DateTime)


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    amount = Column(Integer)
