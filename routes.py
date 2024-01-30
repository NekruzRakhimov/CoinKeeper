import repository
from flask import jsonify, request, render_template, Blueprint


app = Blueprint('routes', __name__)


@app.route('/', methods=['GET'])
def index():
    return {"Status": "Up"}, 200


@app.route('/balances/<int:balance_id>', methods=['GET'])
def get_balance_endpoint(balance_id):
    '''Получение баланса по идентификатору'''
    if not isinstance(balance_id, int):
        return jsonify({'error': 'Invalid balance ID'}), 400

    balance = repository.get_balance(balance_id)
    if balance is None:
        return jsonify({'error': 'Balance not found'}), 404

    return jsonify(balance), 200


@app.route('/balances/<int:balance_id>/increase', methods=['POST'])
def increase_balance_endpoint(balance_id):
    '''Увеличение баланса по идентификатору'''
    if not isinstance(balance_id, int):
        return jsonify({'error': 'Invalid balance ID'}), 400

    data = request.get_json()
    if not data or not isinstance(data.get('amount'), int) or not isinstance(data.get('income_title'), str):
        return jsonify({'error': 'Invalid request data'}), 400

    amount = data['amount']
    income_title = data['income_title']

    repository.increase_balance(balance_id, amount, income_title)
    return jsonify({'message': 'Balance increased successfully'}), 200


@app.route('/expense_categories', methods=['GET'])
def expense_categories():
    '''Получение списка категорий расходов'''
    categories = get_expense_categories()
    return jsonify(categories), 200


@app.route('/expenses/<int:category_id>', methods=['GET'])
def expenses_by_category(category_id):
    '''Получение расходов по идентификатору категории'''
    if not isinstance(category_id, int):
        return jsonify({'error': 'Invalid category ID'}), 400

    expenses = repository.get_expenses_by_category(category_id)
    return jsonify(expenses), 200


@app.route('/expenses/<int:expense_id>/pay', methods=['POST'])
def pay_expense_endpoint(expense_id):
    '''Оплата расхода по идентификатору'''
    if not isinstance(expense_id, int):
        return jsonify({'error': 'Invalid expense ID'}), 400

    repository.pay_expense(expense_id)
    return jsonify({'message': 'Expense paid successfully'}), 200


@app.route('/expenses', methods=['GET'])
def get_expenses_endpoint():
    '''Получение списка расходов'''
    expenses = repository.get_expenses()
    return jsonify(expenses), 200


@app.route('/incomes', methods=['GET'])
def incomes():
    '''Получение списка доходов'''
    incomes = repository.get_all_incomes()
    return jsonify(incomes), 200


@app.route('/filtered_expenses', methods=['POST'])
def filtered_expenses():
    '''Обработчик для эндпоинта '/filtered_expenses' с методом POST'''

    # Получение данных из тела JSON-запроса
    data = request.get_json()

    # Извлечение параметров из данных запроса
    category_id = data.get('category_id')
    min_amount = data.get('min_amount')
    max_amount = data.get('max_amount')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Вызов функции filter_expenses с передачей извлеченных параметров
    expenses = repository.filter_expenses(
        category_id, min_amount, max_amount, start_date, end_date)

    # Возвращение отфильтрованных расходов в формате JSON
    return jsonify(expenses), 200


@app.route('/balances', methods=['GET'])
def get_all_balances_endpoint():
    '''Получение списка всех балансов'''
    balances = repository.get_all_balances()
    return jsonify(balances), 200
