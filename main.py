from datetime import date
from readTimes import getSessionDate, getSessionTime
from writeSession import getSessions
from files import openLogFile, writeLogFile
# from dbfuncs import Datos
# from writesesion import Sesion
# from mysql.connector import Error

# logPath: str = '~/RetroStats/logs/game_stats.log'

logPath: str = 'logs/game_stats.log'

def main():

    # Process logs file
    rows: list[str] = openLogFile(logPath)
    print("Procesando las horas...")
    print('horas', rows)
    sessionDates: list[str] = getSessionDate(rows)
    print("Sumando las horas de las sesiones....")
    sessionTime: str = getSessionTime(sessionDates)
    if(len(sessionDates)):
        writeLogFile(logPath, sessionDates, sessionTime)

    # Get sessions from the log file
    rows: list[str] = openLogFile(logPath)
    print("Procesando las sesiones...")
    # sesion.procesar(lines)
    # TODO: add proper type
    sessions: list[object] = getSessions(rows)

    # print("Creando las sesiones...")
    # sesiones = sesion.crearSesion()

    #insertar sesion + idnfc BDD
    #el idnfc se lee en la sesion
    # if(sesiones != None):
    #     try:
    #         datos = Datos()
    #         datos.connect()
    #         datos.insertsesion(sesiones)
    #         datos.close()
    #         print("Sesiones confirmadas!")
    #         sesion.confirmarSesion(lines)
    #         print("Sesion insertada correctamente")
    #     except Error as e:
    #         print(e)
    #         print("Ha habido un error al conectar con la base de datos")

if __name__ == "__main__":
    main()