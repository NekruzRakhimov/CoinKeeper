'''from sqlalchemy.orm import sessionmaker
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
            _last_balance = db.query(MoneyMovement).order_by(
                MoneyMovement.id.desc()).filter(
                MoneyMovement.category_id_source == _category_id_source
            ).first()

        if expense:
            new_money_movement = MoneyMovement(
                action="expense",
                category_id=expense.id,
                category_id_source=_category_id_source,
                last_balance=_last_balance - _amount,
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
print(pay_expense("такси", 2, 1, 10, "оплатил такси"))

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
'''
def update_expense(_new_description, _title, _new_title, title_or_description):
    with Session(autoflush=False, bind=engine) as db:
        get_expense_for_update = db.query(Categories).filter_by(title=_title, title_type="expense")
        if title_or_description == 1:
            if get_expense_for_update:
                get_expense_for_update.description = _new_description
                # get_expense_for_update.balance_id = _new_balance_id

            elif get_expense_for_update == 2:
                get_expense_for_update.title = _new_title

            db.commit()
            return True
        else:
            return False
'''

def edit_expense_category(db: Session, category_id: int, new_data: dict):
    category_to_edit = db.query(Categories).filter(Categories.id == category_id).first()
    if category_to_edit:
        for key, value in new_data.items():
            setattr(category_to_edit, key, value)
        db.commit()
        db.refresh(category_to_edit)
        return category_to_edit

def edit_income_category(db: Session, category_id: int, new_data: dict):
    category_to_edit = db.query(Incomes).filter(Incomes.id == category_id).first()
    if category_to_edit:
        for key, value in new_data.items():
            setattr(category_to_edit, key, value)
        db.commit()
        db.refresh(category_to_edit)
        return category_to_edit


def pay_expense(description, _get_balance_id):
    with Session(autoflush=False, bind=engine) as db:
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

def delete_expense_categorie(_title, _get_balance_id):
    with Session(autoflush=False, bind=engine) as db:
        expense = db.query(Categories).filter_by(title=_title, title_type="expense").first()
        db.delete(expense)

def delete_expense(_title, _get_balance_id):
    with Session(autoflush=False, bind=engine) as db:
        expense = db.query(Expenses).filter_by(title=_title).first()
        if expense.amount <= 0:
            db.delete(expense)
        else:
            pay_expense(_title, _get_balance_id)

def pay_income(_title, _get_balance_id):
    with Session() as db:
        try:
            income = db.query(Incomes).filter_by(title=_title).first()
            if income:
                balance = db.query(Balances).filter_by(id=_get_balance_id).first()
                if balance.balance >= income.amount:
                    balance.balance += income.amount
                    db.delete(income)
                    db.commit()
                    return True
                else:
                    return False
            else:
                return False
        except BaseException as e:
            return e

def delete_income_categorie(_title, _get_balance_id):
    with Session(autoflush=False, bind=engine) as db:
        income = db.query(Categories).filter_by(title=_title, title_type="income").first()
        db.delete(income)

def delete_income(_title, _get_balance_id):
    with Session(autoflush=False, bind=engine) as db:
        income = db.query(Incomes).filter_by(title=_title, title_type="income").first()
        if income.amount <= 0:
            db.delete(income)

        else:
            pay_income(_title, _get_balance_id)



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
            balances = db.query(Balances).all()
            list_balances = []
            for balance in balances:
                dict_balances = {
                    'id': balance.id,
                    'title': balance.title,
                    'balance': balance.balance
                }
                list_balances.append(dict_balances)
            return list_balances
        except BaseException as e:
            return e

def get_uniq_balances(_title):
    with Session() as db:
        try:
            balance = db.query(Balances).filter_by(title=_title).first()
            list_balance = []
            dict_balance = {
                'id': balance.id,
                'title': balance.title,
                'balance': balance.balance
            }
            list_balance.append(dict_balance)
            return list_balance
        except BaseException as e:
            return e

def get_expense_categorie():
    with Session() as db:
        try:
            expense_categories = db.query(Categories).filter_by(title_type='expense').all()
            list_expense_categories = []
            for expense_categorie in expense_categories:
                dict_expense_categorie = {
                    'id': expense_categorie.id,
                    'title': expense_categorie.title,
                    'title_type': expense_categorie.title_type,
                    'description': expense_categorie.description
                }
                list_expense_categories.append(dict_expense_categorie)
            return list_expense_categories
        except BaseException as e:
            return e

def get_incomes():
    with Session() as db:
        try:
            incomes = db.query(Incomes).all()
            list_incomes = []
            for income in incomes:
                dict_incomes = {
                    'id': income.id,
                    'title': income.title,
                    'amount': income.amount
                }
                list_incomes.append(dict_incomes)
            return list_incomes
        except BaseException as e:
            return e

def get_uniq_income(_title):
    with Session() as db:
        try:
            income = db.query(Incomes).filter_by(title=_title).first()
            return income
        except BaseException as e:
            return e

def get_uniq_expense(_title):
    with Session() as db:
        try:
            expense = db.query(Expenses).filter_by(title=_title).first()
            return expense
        except BaseException as e:
            return e



# print(get_balances())
# print(get_expenses())
# top_balance(1, 100)