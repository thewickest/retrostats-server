import mysql.connector

class Database(object):
    def _init_(self,connection,cursor):
        self.connection = connection
        self.cursor = cursor
        
    def connect(self):
        print("Conectando con la base de datos...")
        try:
            self.connection = mysql.connector.connect(host='192.168.3.14', 
                                                        database='retrostats', 
                                                        user='retrostats', 
                                                        password='retrostats')
            self.cursor = self.connection.cursor(prepared=True)
        except Exception as e:
            print(e)
    def insertsesion(self,sesiones):
        # TODO: another fetch to the api
        print("Insertando sesiones...")
        for sesion in sesiones:
            query = """INSERT INTO sesion (id_s, id_u, id_j, fechaInicio, tiempo, score)
                        VALUES (%s,%s,%s,%s,%s,%s)"""
            self.cursor.execute(query,sesion)

    def takeid(self,valor):
        # TODO: this should be changed by a fetch to the api
        print("Extrayendo id del usuario...")
        query = """SELECT id FROM usuario WHERE id_nfc = %s"""
        self.cursor.execute(query,[float(valor)])
        return self.cursor.fetchall()[0][0]
        
    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
