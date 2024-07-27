#Un archivo de prueba

import mariadb
import os

try:
    os.system('sudo systemctl start mariadb')

except:
    print('[!] Invalid command.')

try:
    conn = mariadb.connect(
<<<<<<< HEAD
    user='Yh0xr',
    password='12345',
    host='localhost',
    port=3306,
    database='prueba'
=======
        user = 'Yh0xr',
        password = '12345',
        host = 'localhost',
        port = 3306,
>>>>>>> 4dfc481a18bf5ff53390cd3ff93ef0eabcbf9c26
    )
    c = conn.cursor()
    c.execute('DROP DATABASE IF EXISTS prueba;')
    c.execute('CREATE DATABASE IF NOT EXISTS prueba;')
    c.execute('USE prueba;')

    print('Connection succesful')
except mariadb.Error as e:
<<<<<<< HEAD
    print(e)

c.execute('create table datos('
          'id int primary key, nombre varchar(20), cedula varchar (20)'
        ');')

c.execute('insert into datos(id, nombre, cedula)'
          'values (1, "Yhoxin", "28289663"), (2, "Josmer", "29748403");')

c.execute('select * from datos;')
=======
    print(e)
>>>>>>> 4dfc481a18bf5ff53390cd3ff93ef0eabcbf9c26
