from connection import Session, engine
from models import Expenses, Balances, Incomes, ExpensesCategories
from sqlalchemy import and_, func
from datetime import datetime
from pprint import pprint


def get_all_balances():
    '''Получение списка всех балансов:'''
    with Session(autoflush=False, bind=engine) as db:
        balances = db.query(Balances).all()
    return balances


def increase_balance(_balance_id, _amount, _income_title):
    '''Пополнение баланса:'''
    with Session(autoflush=False, bind=engine) as db:
        balance = db.query(Balances).get(_balance_id)
        balance.balance += _amount

        income = Incomes(title=_income_title, amount=_amount)
        db.add(income)

        db.commit()


def get_expense_categories():
    '''Получение списка категорий расходов:'''
    with Session(autoflush=False, bind=engine) as db:
        categories = db.query(ExpensesCategories).all()
    return categories


def get_expenses():
    '''Получение списка расходов:'''
    with Session(autoflush=False, bind=engine) as db:
        expenses = db.query(Expenses).all()
    return expenses


def pay_expenses(_expense_ids):
    '''Оплата расходов:'''
    with Session(autoflush=False, bind=engine) as db:
        expenses = db.query(Expenses).filter(
            Expenses.id.in_(_expense_ids)).all()
        for expense in expenses:
            balance = db.query(Balances).get(expense.balance_id)
            balance.balance -= expense.amount
        db.commit()


def filter_expenses(_category_id=None, _min_amount=None, _max_amount=None, _start_date=None, _end_date=None):
    '''Получение списка расходов с фильтрацией:'''
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Expenses)
        if _category_id is not None:
            query = query.filter(Expenses.category_id == _category_id)
        if _min_amount is not None:
            query = query.filter(Expenses.amount >= _min_amount)
        if _max_amount is not None:
            query = query.filter(Expenses.amount <= _max_amount)
        if _start_date is not None:
            query = query.filter(Expenses.created_at >= _start_date)
        if _end_date is not None:
            query = query.filter(Expenses.created_at <= _end_date)
        expenses = query.all()
    return expenses


def get_all_incomes():
    '''Получения списка всех доходов:'''
    with Session(autoflush=False, bind=engine) as db:
        incomes = db.query(Incomes).all()
    return incomes


def get_balance(_balance_id):
    '''Получение баланса по идентификатору'''
    with Session(autoflush=False, bind=engine) as db:
        balance = db.query(Balances).get(_balance_id)
    return balance


def pay_expense(_expense_id):
    '''Оплата расхода по идентификатору'''
    with Session(autoflush=False, bind=engine) as db:
        expense = db.query(Expenses).get(_expense_id)
        balance = db.query(Balances).get(expense.balance_id)
        balance.balance -= expense.amount
        db.commit()
