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

            new_category = Category(title=_title, description=_description, type_of_title=_title_of_type)
            db.add(new_category)
            db.commit()
            return new_category

    except BaseException as e:
        return e

add_category("Cash", 2, "money which is in my hand")
add_category("такси", 1, "довез до дома")




def pay_expense(_title, _get_balance_id, _category_id_source, _amount, _description):
    with Session(autoflush=False, bind=engine) as db:
        expense = db.query(Category).filter(Category.type_of_title == "expense", Category.title == _title).first()
        with Session(autoflush=False, bind=engine) as db:
            _last_balance = db.query(MoneyMovement).order_by(MoneyMovement.id.desc()).filter(
                MoneyMovement.category_id_source == _category_id_source).first()

        _last_balance = _last_balance.__dict__['last_balance']
        if expense:
            new_money_movement = MoneyMovement(
                action="expense",
                category_id=expense.id,
                category_id_source=_category_id_source,
                last_balance=_last_balance,
                amount=_amount,
                description=_description,
                created_at=datetime.now()
            )

            db.add(new_money_movement)
            db.commit()
            return True
        else:
            return False


def get_balance_for_check():
    with Session(autoflush=False, bind=engine) as db:
        money_movement_list = []
        money_movements = db.query(MoneyMovement).all()
        for money_movement in money_movements:
            get_check = {
                'id': money_movement.id,
                'created_at': money_movement.created_at,
                'action': money_movement.action,
                'category_id': money_movement.category_id,
                'category_id_source': money_movement.category_id_source,
                'last_balance': money_movement.last_balance,
                'amount': money_movement.amount,
                'description': money_movement.description
            }
            money_movement_list.append(get_check)

        return money_movement_list


print(get_balance_for_check())
print(pay_expense("такси", 2, 2, 10, "оплатил такси"))

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

# add_category("Cash", 2, "money which is in my hand")
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

# print(get_balances())
# print(get_expenses())
# top_balance(1, 100)
