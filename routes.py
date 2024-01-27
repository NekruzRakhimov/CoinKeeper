import random
import repository
from models import Accounts
from flask import jsonify, request, render_template, Blueprint

app = Blueprint('routes', __name__)


@app.route('/', methods=['GET'])
def index():
    return {"Status": "Up"}, 200


# Получение списка балансов
@app.route('/balances', methods=['GET'])
def get_balances():
    serialized_balances = []
    # balances = repository.get_balances()
    balances = [{'id': 1,
                 'title': 'Мой баланс',
                 'balance': 10000},
                {'id': 2,
                 'title': 'Мой баланс',
                 'balance': 20000}]

    # for balance in balances:
    #     dict_balance = balance.__dict__
    #     del dict_balance['_sa_intence_state']
    #     serialized_balances.append(dict_balance)
    return {'Balances': serialized_balances}, 200


# Получение списка расходов
@app.route('/incomes', methods=['GET'])
def get_incomes():
    serialized_incomes = []
    all_incomes = repository.get_incomes()
    for income in all_incomes:
        dict_incomes = income.__dict__
        serialized_incomes.append(dict_incomes)
    return {'Incomes': serialized_incomes}, 200