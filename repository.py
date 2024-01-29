# import psycopg2
from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from connection import engine
from models import Category, MoneyMovement
from datetime import datetime
from security import *
from pprint import pprint


def add_category(_title, _title_type, _description=''):
    """
    In table for 4 colums
    id | title | title_type | description
    --------------------------------------
    1  | Freelance | income | 
    2  | Taxi      | expense| 
    3  | Cash      | balance| money which is in my hand


    title_type is case sensitive be carefule while typing
    """
    with Session(autoflush=False, bind=engine) as db:
        db.add(Category(title=_title, title_type=_title_type,
               description=_description))
        db.commit()


def categories_dict(_title_type='') -> list:
    """
    Returning all categories in form list and each element is dict
    """
    with Session(autoflush=False, bind=engine) as db:
        categories = db.query(Category).filter(
            Category.title_type.ilike("%{}".format(_title_type)))
        free_list = []
        for category in categories:
            category = category.__dict__
            del category['_sa_instance_state']
            free_list.append(category)

    return free_list


def category_info_return(_title):
    "Takes name of category and return all info about category in dict"
    with Session(autoflush=False, bind=engine) as db:
        item = db.query(Category).filter(Category.title == _title).first()
        item = item.__dict__
        del item['_sa_instance_state']
        return item


def add_actions(_action: str, _category_id: int, _category_id_source: int, _amount: int, _description=""):

    def get_last_balance(_category_id_source):
        with Session(autoflush=False, bind=engine) as db:
            _last_balance = db.query(MoneyMovement).order_by(MoneyMovement.id.desc()).filter(
                MoneyMovement.category_id_source == _category_id_source).first()
        return _last_balance.__dict__['last_balance']

    if _action.lower() == 'income':
        with Session(autoflush=False, bind=engine) as db:
            db.add(MoneyMovement(created_at=datetime.utcnow(), action=_action, category_id=_category_id, category_id_source=_category_id_source,
                                 last_balance=get_last_balance(_category_id_source)+_amount, amount=_amount, description=_description))
            db.commit()

    elif _action.lower() == 'expense':
        with Session(autoflush=False, bind=engine) as db:
            db.add(MoneyMovement(created_at=datetime.utcnow(), action=_action, category_id=_category_id, category_id_source=_category_id_source,
                                 last_balance=get_last_balance(_category_id_source)-_amount, amount=_amount, description=_description))
            db.commit()

    elif _action.lower() == 'move':
        with Session(autoflush=False, bind=engine) as db:
            now = datetime.utcnow()
            db.add(MoneyMovement(created_at=now, action=_action, category_id=_category_id, category_id_source=_category_id_source,
                                 last_balance=get_last_balance(_category_id_source)-_amount, amount=_amount, description=_description))
            db.add(MoneyMovement(created_at=now, action=_action, category_id=_category_id_source, category_id_source=_category_id,
                                 last_balance=get_last_balance(_category_id)+_amount, amount=_amount, description=_description))
            db.commit()


'''
if program gets slow we can use it for make faster



conn = psycopg2.connect(dbname=dbname_app, user=user_app,
                        password=password_app, host=host_app, port=port_app)
cur = conn.cursor()
cur.execute("""SELECT last_balance FROM MoneyMovement
WHERE id = (SELECT MAX(id) FROM MoneyMovement) AND category_id_source = 1;
""")

print(cur)
cur.close()
conn.close()

'''


def report_expense_bydate_and_bytitle(from_date, till_date, title_name='') -> list:
    '''from_date and tille_date takes date time in fromat year-./month-./day
        if you need to know exact what type of category's amount just type name in title_name
    '''

    with Session(autoflush=False, bind=engine) as db:
        result = db.query(Category.title, func.sum(MoneyMovement.amount)).join(MoneyMovement,
                                                                               Category.id == MoneyMovement.category_id).filter(Category.title.ilike("%{}%".format(title_name)),
                                                                                                                                MoneyMovement.action == 'expense',
                                                                                                                                MoneyMovement.created_at.between(from_date, till_date)).group_by(Category.title).all()
    return result


def report_balance_bydate(balance_date, name_balance=''):
    'Need to work !!! some problems'

    with Session(autoflush=False, bind=engine) as db:

        subquery = (db.query(MoneyMovement.category_id_source,
                             func.max(MoneyMovement.created_at).label(
                                 'latest_created_at')
                             ).group_by(MoneyMovement.category_id_source).subquery()
                    )

        result = (db.query(Category.title, MoneyMovement.last_balance)
                  .join(subquery, Category.id == subquery.c.category_id_source)
                  .join(MoneyMovement, (subquery.c.category_id_source == MoneyMovement.category_id_source)
                        & (subquery.c.latest_created_at == MoneyMovement.created_at)
                        ).filter(Category.title.ilike("%{}%".format(name_balance)), MoneyMovement.created_at <= balance_date)
                  .all()
                  )

    return result


def report_income_bydare_and_bytitle(from_date, till_date, title_name='') -> list:
    '''from_date and tille_date takes date time in fromat year-./month-./day
        if you need to know exact what type of category's amount just type name in title_name
    '''
    with Session(autoflush=False, bind=engine) as db:
        result = db.query(Category.title, func.sum(MoneyMovement.amount)).join(MoneyMovement,
                                                                               Category.id == MoneyMovement.category_id).filter(Category.title.ilike("%{}%".format(title_name)),
                                                                                                                                MoneyMovement.action == 'income', MoneyMovement.amount > 0,
                                                                                                                                MoneyMovement.created_at.between(from_date, till_date)).group_by(Category.title).all()
    return result
