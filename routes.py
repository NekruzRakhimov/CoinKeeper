import repository
from flask import jsonify, request, Blueprint

app = Blueprint('routes', __name__)


# Добавление новой категории расходов
@app.route('/categories/create', methods=['POST'])
def add_category():
    data = request.get_json()
    title = data['title']
    description = data['description']
    repository.add_category(title, description)
    return {'status': 'successfully added'}, 201


# Получение списка категорий расходов
@app.route('/expense_categories', methods=['GET'])
def expense_categories():
    categories = repository.get_expense_categories()
    return jsonify(categories), 200


# Получение списка расходов
@app.route('/expenses', methods=['GET'])
def get_expenses_endpoint():
    expenses = repository.get_expenses()
    return jsonify(expenses), 200


# Получение баланса по идентификатору
@app.route('/balances/<int:balance_id>', methods=['GET'])
def get_balance_endpoint(balance_id):
    if not isinstance(balance_id, int):
        return jsonify({'error': 'Invalid balance ID'}), 400

    balance = repository.get_balance(balance_id)
    if balance is None:
        return jsonify({'error': 'Balance not found'}), 404

    return jsonify(balance), 200


# Увеличение баланса по идентификатору
@app.route('/balances/<int:balance_id>/increase', methods=['POST'])
def increase_balance_endpoint(balance_id):
    if not isinstance(balance_id, int):
        return jsonify({'error': 'Invalid balance ID'}), 400

    data = request.get_json()
    if not data or not isinstance(data.get('amount'), int) or not isinstance(data.get('income_title'), str):
        return jsonify({'error': 'Invalid request data'}), 400

    amount = data['amount']
    income_title = data['income_title']

    repository.increase_balance(balance_id, amount, income_title)
    return jsonify({'message': 'Balance increased successfully'}), 200


# Получение расходов по идентификатору категории
@app.route('/expenses/<int:category_id>', methods=['GET'])
def expenses_by_category(category_id):
    if not isinstance(category_id, int):
        return jsonify({'error': 'Invalid category ID'}), 400
    expenses = repository.get_expense_categories(category_id)
    return jsonify(expenses), 200


# Оплата расхода по идентификатору
@app.route('/expenses/<int:expense_id>/pay', methods=['POST'])
def pay_expense_endpoint(expense_id):
    if not isinstance(expense_id, int):
        return jsonify({'error': 'Invalid expense ID'}), 400
    repository.pay_expense(expense_id)
    return jsonify({'message': 'Expense paid successfully'}), 200


# Получение списка доходов
@app.route('/incomes', methods=['GET'])
def incomes():
    incomes = repository.get_all_incomes()
    return jsonify(incomes), 200


# Отфильтровать расходы
@app.route('/filtered_expenses', methods=['POST'])
def filtered_expenses():
    data = request.get_json()
    # Извлечение параметров из данных запроса
    category_id = data.get('category_id')
    min_amount = data.get('min_amount')
    max_amount = data.get('max_amount')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    expenses = repository.filter_expenses(category_id, min_amount, max_amount, start_date, end_date)
    return jsonify(expenses), 200


@app.route('/balances', methods=['GET'])
def get_all_balances_endpoint():
    balances = repository.get_all_balances()
    return jsonify(balances), 200
