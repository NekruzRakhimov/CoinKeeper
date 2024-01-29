from sqlalchemy.orm import sessionmaker
from connection import engine
from models import *
from datetime import datetime

Session = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def add_category(_title, _title_of_type, _description):
    try:
        with Session() as db:
            if _title_of_type == 1:
                _title_of_type = "expense"
            elif _title_of_type == 2:
                _title_of_type = "balance"
            elif _title_of_type == 3:
                _title_of_type = "income"
            else:
                print("Unexpected _title_of_type")
                return False

            new_categorie = Category(title=_title, description=_description, title_of_type=_title_of_type)
            db.add(new_categorie)
            db.commit()
            return new_categorie

    except BaseException as e:
        return e

add_category("Такси", 1, "довез до дома")
'''
def add_income(_title, _description):
    try:
        with Session() as db:
            new_categorie = Categories(title=_title, amount=amount)
            db.add(new_categorie)
            db.commit()
            return new_categorie

    except BaseException as e:
        return e
'''


# add_balance("Наличка", 500)


# add_expense(1, 1500, 1)

def pay_expense(_title, _get_balance_id, _category_id_source,amount):
    with Session() as db:
        expense = db.query(Category).filter_by(title_of_type="expense", title=_title)
        if expense:
            get_last_balance = db.query(MoneyMovement).
            new_money_movement = MoneyMovement(action="expense", category_id=expense.id, category_id_source=_category_id_source, last_balance)

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

# print(get_balances())
# print(get_expenses())
# top_balance(1, 100)
