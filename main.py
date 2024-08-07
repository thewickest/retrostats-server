from datetime import date
from readTimes import openLogFile, writeLogFile, getSessionDate, getSessionTime
# from dbfuncs import Datos
# from writesesion import Sesion
# from mysql.connector import Error

# logPath: str = '~/RetroStats/logs/game_stats.log'

logPath: str = 'logs/game_stats.log'

def main():

    # horas = Times()
    rows: list[str] = openLogFile(logPath)
    print("Procesando las horas...")
    sessionDates: list[str] = getSessionDate(rows)
    print("Sumando las horas de las sesiones....")
    sessionTime: str = getSessionTime(sessionDates)
    writeLogFile(logPath, sessionDates, sessionTime)

    #obtener sesion
    # sesion = Sesion()
    # lines = sesion.openlog()
    # print("Procesando las sesiones...")
    # sesion.procesar(lines)

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