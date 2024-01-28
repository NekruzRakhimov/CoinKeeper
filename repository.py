from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from connection import engine
from models import Category, MoneyMovement
from datetime import datetime
#import psycopg2
from security import *


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


def category_id_return(_title):
    with Session(autoflush=False, bind=engine) as db:
        _id = db.query(Category).filter(Category.title == _title).first()
        _id = _id.__dict__['id']
        return _id


def add_actions(_action, _category_id, _category_id_source, _amount, _description=""):
    def get_last_balance(_category_id_source):
        with Session(autoflush=False, bind=engine) as db:
            _last_balance = db.query(MoneyMovement).order_by(MoneyMovement.id.desc()).filter(
                MoneyMovement.category_id_source == _category_id_source).first()

        return _last_balance.__dict__['last_balance']

    with Session(autoflush=False, bind=engine) as db:
        db.add(MoneyMovement(created_at=datetime.utcnow(), action=_action, category_id=_category_id, category_id_source=_category_id_source,
               last_balance=get_last_balance(_category_id_source)+_amount, amount=_amount, description=_description))
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
