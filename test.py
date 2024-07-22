#Un archivo de prueba

import mariadb

try:
    conn = mariadb.connect(
        user = 'Yh0xr',
        password = '12345',
        host = 'localhost',
        port = 3306,
    )
    c = conn.cursor()
    c.execute('DROP DATABASE IF EXISTS prueba;')
    c.execute('CREATE DATABASE IF NOT EXISTS prueba;')
    c.execute('USE prueba;')

    print('Connection succesful')
except mariadb.Error as e:
    print(e)