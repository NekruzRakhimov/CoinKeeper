# Приложение COINKEEPER

## Описание:

CoinKeeper - "Coin" (монета) и "keeper" (хранитель) - ваш личный хранитель финансов.

### Структура:

ExpensesCategories
    id, title, description

Expenses
    id, description, category_id, amount, balance_id, created_at

Balances
    id, title, balance

Incomes
    id, title, amount

### Выполняемые задачи проекта:

1. Список Балансов
2. Пополнение баланса
3. Получение списка категорий расходов
4. Получение списка расходов
5. Оплатить расход
6. Получить список расходов(фильтры по категориям, по сумме, по дате)

### Стек проекта:

http    -   flask
db      -   psycopg2

