from readtimes import Times
from nfc import NFC
from dbfuncs import Datos
from writesesion import Sesion
from readscores import ScoreReader
from mysql.connector import Error
def main():

    horas = Times()
    rows = horas.openlog()
    print("Procesando las horas...")
    horainicio = horas.process(rows)
    print("Sumando las horas de las sesiones....")
    horas.sumarhoras(horainicio)
    horas.writelog()

    #obtener sesion
    sesion = Sesion()
    lines = sesion.openlog()
    print("Procesando las sesiones...")
    sesion.procesar(lines)

    print("Creando las sesiones...")
    sesiones = sesion.crearSesion()

    #insertar sesion + idnfc BDD
    #el idnfc se lee en la sesion
    if(sesiones != None):
        try:
            datos = Datos()
            datos.connect()
            datos.insertsesion(sesiones)
            datos.close()
            print("Sesiones confirmadas!")
            sesion.confirmarSesion(lines)
            print("Sesion insertada correctamente")
        except Error as e:
            print(e)
            print("Ha habido un error al conectar con la base de datos")

if __name__ == "__main__":
    main()