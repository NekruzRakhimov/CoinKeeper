from security import dbname_app, user_app, password_app, host_app, port_app
from sqlalchemy import create_engine, Column, String, Integer, SmallInteger, Numeric, Boolean, DateTime, ForeignKey, or_
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

# Атрибут подключения для движка SQLAlchemy.
DATABASE_URL = f"postgresql://{user_app}:{password_app}@{host_app}:{port_app}/{dbname_app}"

# Создаём движок SQLAlchemy.
engine = create_engine(DATABASE_URL, echo=False)
