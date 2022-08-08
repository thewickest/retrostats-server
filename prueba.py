import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='192.168.3.15', 
                                            database='myarcadesystem', 
                                            user='every', 
                                            password='every')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    
    #empezamos la query que queramos hacer
    query = "select * from myarcadesystem.usuario"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    #imprimimos por pantalla
    for record in records:
        print(record)


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
