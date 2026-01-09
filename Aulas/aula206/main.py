import os

import pymysql
import pymysql.cursors
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MY_HOST'],
    user=os.environ['MYSQL_USER'],
    port=int(os.environ['MY_PORT']),
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    # cursorclass=pymysql.cursors.DictCursor,
    # cursorclass=pymysql.cursors.SSDictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )

    #CUIDADO: isso limpa a tabela
        cursor.execute(F'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) '
        'VALUES '
        '(%s, %s) '
        )
        data = ("Luiz", 18)
        cursor.execute(sql, data)

    connection.commit()


    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) '
        'VALUES '
        '(%(name)s, %(age)s) '
        )
        data2 = {
            "name": "Le",
            "age": 37,
        }
        cursor.execute(sql, data2)

    connection.commit()

    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) '
        'VALUES '
        '(%(name)s, %(age)s) '
        )
        data3 = (
        {"name": "Ana","age": 30},
        {"name": "Silvano","age": 23},
        {"name": "Júlia","age": 27},
        )
        cursor.executemany(sql, data3)

    connection.commit()

    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) '
        'VALUES '
        '(%s, %s) '
        )
        data4 = (
            ("Siri", 22),
            ("Rakel", 24),
            ("Fernanda", 26),
        )
        cursor.executemany(sql, data4)

    connection.commit()

    # with connection.cursor() as cursor:
    #     sql = f'SELECT * FROM {TABLE_NAME} '
    #     cursor.execute(sql)

    #     data5 = cursor.fetchall()

    #     for row in data5:
    #         print(row)

    # with connection.cursor() as cursor:
    #     minor_id = int(input('Enter the lowest Id: '))
    #     bigger_id = int(input('Enter the highest id: '))
    #     sql = (
    #     f'SELECT * FROM {TABLE_NAME} '
    #     'WHERE id BETWEEN %s AND %s'
    #     )

    #     cursor.execute(sql, (minor_id,bigger_id))

    #     data5 = cursor.fetchall()

    #     for row in data5:
    #         print(row)

    with connection.cursor() as cursor:
        sql = (f'DELETE FROM {TABLE_NAME} '
        'WHERE id = %s'
        )

        cursor.execute(sql,(1))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():
        #     print(row)

    with connection.cursor() as cursor:
        sql = (f'UPDATE {TABLE_NAME} '
        'SET nome=%s, idade=%s '
        'WHERE id = %s'
        )

        cursor.execute(sql,("Alice", 18, 5))

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():
        #     print(row)

        # for row in cursor.fetchall():
        #     _id, name, age = row.values()
        #     print(_id, name, age)

        # for row in cursor.fetchall_unbuffered():
        #     print(row)
        #     if row['id'] == 5:
        #         break

        # print()
        # cursor.scroll(1)
        # # cursor.scroll(-3)
        # for row in cursor.fetchall_unbuffered():
        #     print(row)

        print('last id', cursor.lastrowid)
        print('last id', cursor.rowcount)
        print('last id', cursor.rownumber)

    connection.commit()
        