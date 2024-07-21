#Un archivo de prueba
import mariadb

try:
    conn = pymysql.connect(

    host='localhost',
    port=3306
    )
    print('Connection succesful')

except pymysql.Error as e:
    print(e)