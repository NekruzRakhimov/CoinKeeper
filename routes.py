import repository
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


# Создание категории
@app.route('/categories/create', methods=['POST'])
def add_category():
    data = request.get_json()
    title = data['title']
    title_type = data['title_type']
    description = data['description']
    repository.add_category(title, title_type, description)
    return {'status': 'successfully added'}, 201


# Получение списка расходов
@app.route('/expense', methods=['GET'])
def get_all_expenses():
    serialized_expenses = []
    all_expenses = repository.categories_dict()
    for expense in all_expenses:
        if expense['title_type'] == 'expense':
            serialized_expenses.append(expense)
    return {'expense': serialized_expenses}, 200


# Получение списка доходов
@app.route('/incomes', methods=['GET'])
def get_all_incomes():
    serialized_incomes = []
    all_incomes = repository.categories_dict()
    for income in all_incomes:
        if income['title_type'] == 'income':
            serialized_incomes.append(income)
    return {'incomes': serialized_incomes}, 200


# Получение списка балансов
@app.route('/balances', methods=['GET'])
def get_all_balances():
    serialized_balances = []
    all_balances = repository.categories_dict()
    for balance in all_balances:
        if balance['title_type'] == 'balance':
            serialized_balances.append(balance)
    return {'incomes': serialized_balances}, 200


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
