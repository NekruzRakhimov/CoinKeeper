##### _____________________________________

## Приложение:
# **COIN Keeper**.

##### _____________________________________

## Описание проекта:

**CoinKeeper**  -  "**Coin**" (монета) и "**Keeper**" (хранитель) - Ваш личный хранитель финансов.

##### _____________________________________

**CoinKeeper** - это приложение для учёта финансов, которое поможет вам следить за своими доходами и расходами. Оно предоставляет инструменты для ведения бюджета, установления финансовых целей и отслеживания своей финансовой активности.

**CoinKeeper** позволяет вам записывать все ваши доходы и расходы, категоризировать их, создавать бюджеты и анализировать свои финансовые показатели. Оно также может предоставлять отчеты и статистику о вашей финансовой активности, чтобы помочь вам принимать **осознанные финансовые решения**.

Приложение **CoinKeeper** может быть полезным для управления личными финансами, планирования бюджета, сбережений и достижения финансовых целей.

##### _____________________________________

_-=*=-_

Это **бекендная часть приложения**, которая предоставляет API и обрабатывает бизнес-логику. Здесь нет **фронтендной** части, так как это отдельный компонент или может быть разработан и поддерживается отдельной командой или проектом. Приложение служит интерфейсом для обмена данными с другими приложениями или компонентами. Оно предоставляет набор эндпоинтов ***(URL-адресов)***, по которым другие приложения или клиенты **могут отправлять запросы и получать ответы**.

_-=*=-_

##### _____________________________________

## Структура проекта:

**ExpensesCategories**
*    id, title, description

**Expenses**
*    id, description, category_id, amount, balance_id, created_at

**Balances**
*    id, title, balance

**Incomes**
*    id, title, amount

##### _____________________________________

## Выполняемые задачи проекта:

1. Получение списока всех балансов.
2. Пополнение баланса.
3. Получение списка категорий расходов.
4. Получение списка расходов.
5. Оплата расходов.
6. Получение списка расходов (***фильтрация***: по категориям, по сумме, дате).

##### _____________________________________

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

##### _____________________________________

## Структура проекта по файлам:

### main

* Данный код представляет собой простое приложение **Flask**, которое запускает веб-сервер и определяет маршруты для обработки HTTP-запросов.

* Первым шагом импортируется класс Flask из модуля flask. Затем импортируется переменная **app** из модуля **routes** (это модуль, содержащий определения маршрутов для приложения).

* Далее создается **экземпляр класса** Flask и присваивается переменной **app**. В качестве аргумента конструктору передается __name__, что указывает Flask на то, что это основной модуль или пакет.

* Затем вызывается метод register_blueprint() на объекте **app**, чтобы зарегистрировать маршруты из модуля routes. Регистрация маршрутов позволяет приложению знать, как обрабатывать входящие HTTP-запросы.

* Наконец, проверяется, является ли текущий модуль основным модулем, вызывая __name__ == '__main__'. Если это так, то приложение запускается с помощью метода run() на объекте **app**. В данном случае, включен режим отладки (debug=True) и сервер будет слушать порт 7000.

*   Таким образом, этот код создает ***Flask-приложение***, регистрирует маршруты и запускает сервер для обработки ***HTTP-запросов***.

### connection

* Данный код относится к работе с базой данных в приложении, используя ***SQLAlchemy***.

* Сначала импортируются всё необходимые: dbname_app, user_app, password_app, host_app, port_app из модуля **security**, а также **sessionmaker** и **create_engine** из модуля ***sqlalchemy***.

* Далее определяется строка подключения к базе данных **DATABASE_URL** с использованием значений, полученных из user_app, password_app, host_app, port_app и dbname_app. Эта строка будет содержать информацию, необходимую для установления соединения с базой данных **PostgreSQL**.

* Затем создается экземпляр класса **Engine** из модуля **create_engine** и передается ему **DATABASE_URL** в качестве аргумента. Этот объект (**engine**) представляет собой основной интерфейс к базе данных и будет использоваться для выполнения ***SQL-запросов***.

* Наконец, создается класс **Session** с использованием **sessionmaker**, который связывается с **engine**. Этот класс будет использоваться для создания отдельных сессий (экземпляров) для каждого подключения к базе данных. Сессии позволяют выполнять ***операции чтения и записи данных*** в базу данных.

* Таким образом, данный код устанавливает соединение с базой данных ***PostgreSQL*** с помощью ***SQLAlchemy*** и создает класс **Session**, который будет использоваться для управления подключениями к базе данных в приложении.

### roules

### repository

### models

### readme

* Завершение файла README.md будет реализовано после компановки всех веток в основную **main**.

##### _____________________________________
