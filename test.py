#Un archivo de prueba
import mariadb

try:
    conn = mariadb.connect(
    user='Yh0x',
    password='12345',
    host='localhost',
    port=3306,
    database='prueba'
    )
    print('Connection succesful')
    c = conn.cursor()
    c.execute('drop database if exists prueba;')
    c.execute('create database if not exists prueba;')
    c.execute('use prueba;')

except mariadb.Error as e:
    print(e)

c.close()