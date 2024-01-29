import repository
from models import Accounts
from flask import jsonify, request, render_template, Blueprint


app = Blueprint('routes', __name__)


@app.route('/', methods=['GET'])
def index():
    return {"Status": "Up"}, 200


# Получение списка категорий
@app.route('/categories', methods=['GET'])
def categories_dict():
    serialized_categories = []
    categories = repository.categories_dict()
    for category in categories:
        serialized_categories.append(category)
    return {'Categories': serialized_categories}, 200


# Получение списка расходов
@app.route('/incomes', methods=['GET'])
def get_incomes():
    serialized_incomes = []
    # all_incomes = repository.get_incomes()
    all_incomes = [{'id': 1,
                    'title': 'Мои траты',
                    'amount': 990},
                   {'id': 2,
                    'title': 'Мои траты2',
                    'amount': 1990}]
    for income in all_incomes:
        # dict_incomes = income.__dict__
        # del dict_incomes['_sa_intence_state']
        serialized_incomes.append(income)
    return {'Incomes': serialized_incomes}, 200


# Пополнение баланса
@app.route('/top_up_balance/<int:id>', methods=['PATCH'])
def top_up_balance(_id):
    if not isinstance(_id, int):
        return jsonify({'Error': 'Invalid customer ID format.'}), 400
    data = request.get_json()
    balance = float(data['balance'])
    # repository.top_up_balance(_id, balance)
    return {"status": "balance updated"}, 200


# Оплатить расход
@app.route('/expenses/<int:id>', methods=['PATCH'])
def pay_expenses(_id):
    if not isinstance(_id, int):
        return jsonify({'Error': 'Invalid customer ID format.'}), 400
    # repository.pay_expenses(_id)
    return {"status": "balance withdrawn"}, 200
