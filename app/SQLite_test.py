import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user')
for unit in cursor.fetchall():
    print(unit)
cursor.execute('select * from user')
row = cursor.fetchall()
print(row)
print(row.__len__())

cursor.close()
conn.commit()
conn.close()
