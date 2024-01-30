from sqlalchemy.orm import Session
from connection import engine
from models import ExpensesCategories, Incomes, Balances, Expenses


# Добавления новой категории расходов
def add_category(_title, _description=''):
    with Session(autoflush=False, bind=engine) as db:
        db.add(ExpensesCategories(title=_title, description=_description))
        db.commit()


# Получение списка всех балансов
def get_all_balances():
    with Session(autoflush=False, bind=engine) as db:
        balances = db.query(Balances).all()
    return balances


# Пополнение баланса
def increase_balance(balance_id, amount, income_title):
    with Session(autoflush=False, bind=engine) as db:
        balance = db.query(Balances).get(balance_id)
        balance.balance += amount

        income = Incomes(title=income_title, amount=amount)
        db.add(income)

        db.commit()


# Получение списка категорий расходов
def get_expense_categories():
    with Session(autoflush=False, bind=engine) as db:
        categories = db.query(ExpensesCategories).all()
    return categories


# Получение списка расходов
def get_expenses():
    with Session(autoflush=False, bind=engine) as db:
        expenses = db.query(Expenses).all()
    return expenses


# Оплата расходов
def pay_expenses(expense_ids):
    with Session(autoflush=False, bind=engine) as db:
        expenses = db.query(Expenses).filter(Expenses.id.in_(expense_ids)).all()
        for expense in expenses:
            balance = db.query(Balances).get(expense.balance_id)
            balance.balance -= expense.amount
        db.commit()


# Получение списка расходов с фильтрацией
def filter_expenses(category_id=None, min_amount=None, max_amount=None, start_date=None, end_date=None):
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Expenses)
        if category_id is not None:
            query = query.filter(Expenses.category_id == category_id)
        if min_amount is not None:
            query = query.filter(Expenses.amount >= min_amount)
        if max_amount is not None:
            query = query.filter(Expenses.amount <= max_amount)
        if start_date is not None:
            query = query.filter(Expenses.created_at >= start_date)
        if end_date is not None:
            query = query.filter(Expenses.created_at <= end_date)
        expenses = query.all()
    return expenses


# Получение списка всех доходов
def get_all_incomes():
    with Session(autoflush=False, bind=engine) as db:
        incomes = db.query(Incomes).all()
    return incomes


# Получение баланса по идентификатору
def get_balance(balance_id):
    with Session(autoflush=False, bind=engine) as db:
        balance = db.query(Balances).get(balance_id)
    return balance


# Оплата расхода по идентификатору
def pay_expense(expense_id):
    with Session(autoflush=False, bind=engine) as db:
        expense = db.query(Expenses).get(expense_id)
        balance = db.query(Balances).get(expense.balance_id)
        balance.balance -= expense.amount
        db.commit()
