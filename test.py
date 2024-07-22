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

except mariadb.Error as e:
    print(e)