import psycopg2

from security import dbname_app, user_app, password_app, host_app, port_app


# connect db
# Подключаем базу для дальнейшей работы
conn = psycopg2.connect(dbname=dbname_app,
                        user=user_app,
                        password=password_app,
                        host=host_app,
                        port=port_app)
conn.set_client_encoding('UTF8')
# conn.autocommit = True
cursor = conn.cursor()

##############################
