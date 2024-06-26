
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.2-green)



# **Название проекта: COIN Keeper**.


## Описание проекта:

**CoinKeeper**  -  "**Coin**" (монета) и "**Keeper**" (хранитель) - Ваш личный хранитель финансов.


**CoinKeeper** - это приложение для учёта финансов, которое поможет вам следить за своими доходами и расходами. Оно предоставляет инструменты для ведения бюджета, установления финансовых целей и отслеживания своей финансовой активности.

**CoinKeeper** позволяет вам записывать все ваши доходы и расходы, категоризировать их, создавать бюджеты и анализировать свои финансовые показатели. Оно также может предоставлять отчеты и статистику о вашей финансовой активности, чтобы помочь вам принимать **осознанные финансовые решения**.

Приложение **CoinKeeper** может быть полезным для управления личными финансами, планированием бюджета, сбережений и достижения финансовых целей.


_-=*=-_

Это **бекендная часть приложения**, которая предоставляет API и обрабатывает бизнес-логику. Здесь нет **фронтендной** части, так как это отдельный компонент, который может быть разработан и будет поддерживается отдельной командой, либо проектом. Приложение служит интерфейсом для обмена данными с другими приложениями или компонентами. Оно предоставляет набор эндпоинтов ***(URL-адресов)***, по которым другие приложения или клиенты **могут отправлять запросы** и **получать ответы**.

_-=*=-_


## Структура проекта:
(на начальной стадии проекта)

**ExpensesCategories**
*    id, title, description

**Expenses**
*    id, description, category_id, amount, balance_id, created_at

**Balances**
*    id, title, balance

**Incomes**
*    id, title, amount


## Выполняемые задачи проекта:

1. Получение списка всех балансов.
2. Пополнение баланса.
3. Получение списка категорий расходов.
4. Получение списка расходов.
5. Оплата расходов.
6. Получение списка расходов (***фильтрация***: по категориям, по сумме, по дате).


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


## Структура проекта по файлам (модулям):

### main

* Данный код представляет собой простое приложение **Flask**, которое запускает веб-сервер и определяет маршруты для обработки HTTP-запросов.

* Первым шагом импортируется класс Flask из модуля flask. Затем импортируется переменная **app** из модуля **routes** (это модуль, содержащий определения маршрутов для приложения).

* Далее создается **экземпляр класса** Flask и присваивается переменной **app**. В качестве аргумента конструктору передается __name__, что указывает Flask на то, что это основной модуль или пакет.

* Затем вызывается метод register_blueprint() на объекте **app**, чтобы зарегистрировать маршруты из модуля routes. Регистрация маршрутов позволяет приложению знать, каким образом обрабатывать входящие HTTP-запросы.

* Наконец, проверяется, является ли текущий модуль **основным** модулем, вызывая **__name__ == '__main__'**. Если это так, то приложение запускается с помощью метода run() объекта **app**. В данном случае, включен режим отладки (debug=True) и сервер будет слушать порт 7000.

*   Таким образом, этот код создает ***Flask-приложение***, регистрирует маршруты и запускает сервер для обработки ***HTTP-запросов***.

### connection

* Данный код относится к работе с базой данных в приложении, используя ***SQLAlchemy***.

* Сначала импортируются всё необходимые: dbname_app, user_app, password_app, host_app, port_app из модуля **security**, а также **sessionmaker** и **create_engine** из модуля ***sqlalchemy***.

* Далее определяется строка подключения к базе данных **DATABASE_URL** с использованием значений, полученных из user_app, password_app, host_app, port_app и dbname_app. Эта строка будет содержать информацию, необходимую для установления соединения с базой данных **PostgreSQL**.

* Затем создается экземпляр класса **Engine** из модуля **create_engine** и передается ему **DATABASE_URL** в качестве аргумента. Этот объект (**engine**) представляет собой основной интерфейс к базе данных и будет использоваться для выполнения ***SQL-запросов***.

* Наконец, создается класс **Session** с использованием **sessionmaker**, который связывается с **engine**. Этот класс будет использоваться для создания отдельных сессий (экземпляров) для каждого подключения к базе данных. Сессии позволяют выполнять ***операции чтения и записи данных*** в базу данных.

* Таким образом, данный код устанавливает соединение с базой данных ***PostgreSQL*** с помощью ***SQLAlchemy*** и создает класс **Session**, который будет использоваться для управления подключениями к базе данных в приложении.

### models

#### Класс ExpensesCategories:

Таблица: "expenses_categories"

<= Атрибуты таблицы =>
* id: целочисленное поле, являющееся первичным ключом таблицы.
* title: строковое поле, уникальное, представляет название категории расходов.
* description: строковое поле, представляет описание категории расходов.

#### Класс Incomes:

Таблица: "incomes"

<= Атрибуты таблицы =>
* id: целочисленное поле, являющееся первичным ключом таблицы.
* title: строковое поле, представляет название дохода.
* amount: числовое поле с фиксированной точностью, представляет сумму дохода.
* balance_id: целочисленное поле, являющееся внешним ключом, связанным с полем id таблицы "balances".
* balance: отношение (relationship) к классу Balances, позволяет получить доступ к связанным записям из таблицы "balances".

#### Класс Balances:

Таблица: "balances"

<= Атрибуты таблицы =>
* id: целочисленное поле, являющееся первичным ключом таблицы.
* title: строковое поле, представляет название баланса.
* balance: числовое поле с фиксированной точностью, представляет текущий баланс.
* incomes: отношение (relationship) к классу Incomes, позволяет получить доступ к связанным записям из таблицы "incomes".

#### Класс Expenses:

Таблица: "expenses"

<= Атрибуты таблицы =>
* id: целочисленное поле, являющееся первичным ключом таблицы.
* description: строковое поле, представляет описание расхода.
* category_id: целочисленное поле, являющееся внешним ключом, связанным с полем id таблицы "expenses_categories".
* amount: числовое поле с фиксированной точностью, представляет сумму расхода.
* balance_id: целочисленное поле, являющееся внешним ключом, связанным с полем id таблицы "balances".
* created_at: поле типа DateTime, представляет дату и время создания записи.
* category: отношение (relationship) к классу ExpensesCategories, позволяет получить доступ к связанным записям из таблицы "expenses_categories".
* balance: отношение (relationship) к классу Balances, позволяет получить доступ к связанным записям из таблицы "balances".

**Классы** отражают ***структуру таблиц*** базы данных и связи между ними с использованием ***SQLAlchemy***.
Они предоставляют объектно-реляционное отображение **(ORM)**, которое позволяет взаимодействовать с данными в базе данных с помощью объектов и методов классов.

Таким образом эти таблицы хранят информацию о **категориях** и **движении денежных средств** в **базе данных**.

### roules

Данный модуль представляет собой набор маршрутов (routes) для веб-приложения, созданного с использованием **Flask**, фреймворка для разработки веб-приложений на языке Python.
В данном модуле используется модуль ***repository***, содержащим функции для работы с базой данных и хранения данных. Код определяет различные маршруты (эндпоинты) для обработки ***HTTP-запросов*** и вызывает соответствующие функции из модуля ***repository*** для обработки запросов и возврата данных в формате JSON.

Общая структура кода соответствует парадигме **RESTful API**, где каждому ***URL-адресу*** соответствует определенный **HTTP-метод (GET, POST и т.д.)** и функция для обработки запроса и возврата данных. **Flask** облегчает создание и настройку веб-приложения, предоставляя удобные инструменты для определения маршрутов и обработки запросов.

### repository

Данный модуль представляет собой набор функций для взаимодействия с базой данных с использованием ***SQLAlchemy***. В коде импортируются необходимые модули и классы, а также создается соединение с базой данных.

Каждая **функция** использует контекстные менеджеры ***Session*** и ***with*** для обеспечения **корректного управления сессией** и **соединением с базой данных**, выполняет необходимые запросы и сохраняет изменения с помощью метода **commit()**. Это позволяет обеспечить целостность данных и корректное управление сессией и соединением с базой данных.


### readme

* Файл __README.md__ - это текущий файл, который может быть изменен по мере необходимости, включая сам **"код"**. В процессе разработки и обновления проекта, **README.md** может подвергаться изменениям, чтобы отражать ***актуальную информацию о проекте***, его ***функциональности***, ***инструкции по установке*** и ***использованию***, а также другую полезную информацию для **разработчиков** и **пользователей**. Это важный компонент документации, который помогает улучшить понимание проекта и содействует его успешному использованию. :-)

