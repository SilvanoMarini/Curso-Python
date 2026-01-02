import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

print()



# cursor.execute(F'DELETE FROM {TABLE_NAME} '
#     'WHERE id = "3"'
# )

# cursor.execute(F'DELETE FROM {TABLE_NAME} '
#     'WHERE id = "1"'
# )


cursor.execute(F'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    # print(row)
    _id, name, weigth = row
    print(_id, name, weigth)


# row = cursor.fetchone()
# _id, name, weigth = row
# print(_id, name, weigth)


cursor.close()
connection.close()