# Приложение: **CoinKeeper**.

# Описание проекта:

**CoinKeeper**  -  "**Coin**" (монета) и "**Keeper**" (хранитель) - Ваш личный хранитель финансов.

## Структура проекта:

**ExpensesCategories**
*    id, title, description

**Expenses**
*    id, description, category_id, amount, balance_id, created_at

**Balances**
*    id, title, balance

**Incomes**
*    id, title, amount

## Выполняемые задачи проекта:

1. Получение списока всех балансов.
2. Пополнение баланса.
3. Получение списка категорий расходов.
4. Получение списка расходов.
5. Оплата расходов.
6. Получение списка расходов (***фильтрация***: по категориям, по сумме, дате).

## Стек проекта:

### HTTP - Flask

* **Flask** — это упрощенная платформа ***Python для веб-приложений***, которая обеспечивает
основные возможности маршрутизации <URL-адресов> и визуализации страниц.
**Flask** называют "микро"-платформой, так как она не предоставляет напрямую такие функции,
как проверка форм, абстракция базы данных, проверка подлинности и т. д.
Эти функции предоставляются специальными пакетами Python, называемыми расширениями **Flask**.

### DataBase - SQLAlchemy

* **SQLAlchemy** — это набор инструментов ***Python SQL*** и реляционный преобразователь **объектов**,
который предоставляет разработчикам приложений всю мощь и гибкость **SQL**.

## Структура проекта по файлам:

### main

Данный код представляет собой простое приложение **Flask**, которое запускает веб-сервер и определяет маршруты для обработки HTTP-запросов.

Первым шагом импортируется класс Flask из модуля flask. Затем импортируется переменная **app** из модуля **routes** (предположительно, это модуль, содержащий определения маршрутов для приложения).

Далее создается **экземпляр класса** Flask и присваивается переменной **app**. В качестве аргумента конструктору передается __name__, что указывает Flask на то, что это основной модуль или пакет.

Затем вызывается метод register_blueprint() на объекте **app**, чтобы зарегистрировать маршруты из модуля routes_app. Регистрация маршрутов позволяет приложению знать, как обрабатывать входящие HTTP-запросы.

Наконец, проверяется, является ли текущий модуль основным модулем, вызывая __name__ == '__main__'. Если это так, то приложение запускается с помощью метода run() на объекте **app**. В данном случае, включен режим отладки (debug=True) и сервер будет слушать порт 7000.

Таким образом, этот код создает ***Flask-приложение***, регистрирует маршруты и запускает сервер для обработки ***HTTP-запросов***.

### connection

### roules

### repository

### models


* Завершение файла README.md будет реализовано после компановки всех веток в основную **main**.
