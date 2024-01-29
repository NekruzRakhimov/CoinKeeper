from sqlalchemy.orm import sessionmaker
from connection import engine
from models import *
from datetime import datetime

Session = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def add_expense_categories(_title, _description):
    try:
        with Session() as db:
            new_categorie = Categories(title=_title, description=_description)
            db.add(new_categorie)
            db.commit()
            return new_categorie

    except BaseException as e:
        return e

add_expense_categories("Такси", "довез до дома")

def add_balance(_title, _balance):
    try:
        with Session() as db:
            new_balance = Balances(title=_title, balance=_balance)
            db.add(new_balance)
            db.commit()
            return new_balance

    except BaseException as e:
        return e


# add_balance("Наличка", 500)

def add_expense(_description_id, _amount, _balance_id):
    with Session() as db:
        try:
            get_description = db.query(Categories).filter_by(id=_description_id).first()
            new_expense = Expenses(description=get_description.description, category_id=get_description.id, amount=_amount, balance_id=_balance_id, created_at=datetime.now())
            db.add(new_expense)
            balance = db.query(Balances).filter_by(id=_balance_id).first()
            if balance.balance >= new_expense.amount:
                balance.balance -= new_expense.amount
                db.commit()
            return new_expense
        except BaseException as e:
            return e

# add_expense(1, 1500, 1)

def pay_expense(description, _get_balance_id):
    with Session() as db:
        try:
            expense = db.query(Expenses).filter_by(description=description).first()
            if expense:
                balance = db.query(Balances).filter_by(id=_get_balance_id).first()
                if balance.balance >= expense.amount:
                    balance.balance -= expense.amount
                    db.delete(expense)
                    db.commit()
                    return True
                else:
                    return False
            else:
                return False
        except BaseException as e:
            return e

pay_expense("довез до дома", 1)

def top_balance(_get_balance_id, amount):
    with Session() as db:
        try:
            balance = db.query(Balances).filter_by(id=_get_balance_id).first()
            if 5000 >= amount:
                balance.balance += amount
                db.commit()
                return True
            else:
                return False
        except BaseException as e:
            return e

# top_balance(1, 100)

def get_expenses():
    with Session() as db:
        try:
            expenses = db.query(Expenses).all()
            list_expenses = []
            for expens in expenses:
                dict_expenses = {
                    'id': expens.id,
                    'description': expens.description,
                    'category_id': expens.category_id,
                    'amount': expens.amount,
                    'created_at': expens.created_at
                }
                list_expenses.append(dict_expenses)
            return list_expenses
        except BaseException as e:
            return e

def get_balances():
    with Session() as db:
        try:
            expenses = db.query(Balances).all()
            list_balances = []
            for expens in expenses:
                dict_balances = {
                    'id': expens.id,
                    'title': expens.title,
                    'balance': expens.balance
                }
                list_balances.append(dict_balances)
            return list_balances
        except BaseException as e:
            return e

print(get_balances())
# print(get_expenses())
# top_balance(1, 100)
