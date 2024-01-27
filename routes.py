import random
import repository
from models import Accounts
from flask import jsonify, request, render_template, Blueprint

app = Blueprint('routes', __name__)


@app.route('/', methods=['GET'])
def index():
    return {"Status": "Up"}, 200


# id, description, category_id, amount, balance_id, created_at
categories = [
    {1, "test", 2, 1000, 1122, "27-01-2024"},
    {2, "test", 2, 1000, 1122, "27-01-2024"},
    {3, "test", 2, 1000, 1122, "27-01-2024"}
]


@app.route('/expenses/categories', methods=["GET"])
def get_expenses_categories():
    # categories = repository.get_all_categories()

    serialized_categories = []
    for category in categories:
        serialized_categories.append(category.__dict__)
    return serialized_categories
