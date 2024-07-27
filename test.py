#Un archivo de prueba

import mariadb
import os

try:
    os.system('sudo systemctl start mariadb')

except:
    print('[!] Invalid command.')

try:
    conn = mariadb.connect(
    user='Yh0xr',
    password='12345',
    host='localhost',
    port=3306,
    database='prueba'
    )
    c = conn.cursor()
    c.execute('DROP DATABASE IF EXISTS prueba;')
    c.execute('CREATE DATABASE IF NOT EXISTS prueba;')
    c.execute('USE prueba;')

    print('Connection succesful')
except mariadb.Error as e:
    print(e)

c.execute('create table datos('
          'id int primary key, nombre varchar(20), cedula varchar (20)'
        ');')

c.execute('insert into datos(id, nombre, cedula)'
          'values (1, "Yhoxin", "28289663"), (2, "Josmer", "29748403");')

c.execute('select * from datos;')
