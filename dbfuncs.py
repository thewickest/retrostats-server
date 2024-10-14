import mysql.connector
from variables import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER, DATABASE_HOST

class Database(object):
    def _init_(self,connection,cursor):
        self.connection = connection
        self.cursor = cursor
        
    def connect(self):
        print("Connecting with the backup database...")
        try:
            self.connection = mysql.connector.connect(  host = DATABASE_HOST, 
                                                        database = DATABASE_NAME,
                                                        user = DATABASE_USER, 
                                                        password = DATABASE_PASSWORD )
            self.cursor = self.connection.cursor(prepared=True)
        except Exception as e:
            print(e)
    def insertSessions(self,sessions):
        print("Creating backup sessions...")
        backupSessions = []
        for session in sessions:
            query = """INSERT INTO sessions (initDate, duration, score, gameId, gameName, gameEmulator, gamePath, userId, state) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            statement = (
                session['initDate'], 
                session['duration'], 
                session['score'], 
                session['gameId'], 
                session['gameName'], 
                session['gameEmulator'], 
                session['gamePath'], 
                session['userId'],
                'CREATED'
            )
            self.cursor.execute(query, statement)
            backupSessions.append({'id': self.cursor.lastrowid, 'session': session})
        return backupSessions

    def updateSessions(self, sessions, state):
        print("Updating backup sessions...")
        for session in sessions:
            query = 'UPDATE sessions SET state = %s WHERE id = %s'
            self.cursor.execute(query, (state, session['id']))

    def getErrorSessions(self):
        query = 'SELECT * FROM sessions WHERE state = "ERROR"'
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]

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
