import sqlite3
from pathlib import Path


# Build an absolute path to the SQLite database based on the script location


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'custumers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()



cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    ' id INTEGER PRIMARY KEY AUTOINCREMENT,'
    ' name TEXT,'
    ' weigth REAL'
    ')'
)
connection.commit()

cursor.execute(
    F'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

sql = f'INSERT INTO {TABLE_NAME} (name, weigth) VALUES (:nome, :peso)'


# cursor.execute(sql, ['Silvano', 68])
# cursor.executemany(sql, [['Silvano', 68], ['Rakel', 65]])
# cursor.execute(sql, {'nome':'Silvano', 'peso':68})
cursor.executemany(sql,(
    {'nome':'Silvano', 'peso':68}, 
    {'nome':'Rakel', 'peso':65},
    {'nome':'Ana', 'peso':60},
    {'nome':'Joana', 'peso':55},
    {'nome':'João', 'peso':72.2},
    {'nome':'Paulo', 'peso':56.6},
)
)


cursor.execute(
    F'DELETE FROM {TABLE_NAME} '
    'WHERE id = "4"'
)

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    ' SET name="Carla", weigth=61.45 '
    'WHERE id= "3"'
)


cursor.execute(F'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weigth = row
    print(_id, name, weigth)


connection.commit()


cursor.close()
connection.close()