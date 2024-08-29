from datetime import datetime
from readScores import getScores
from pathlib import Path
from constants import info, error
from api.api import getGameBySlug, login, getPlayerByNfc
from variables import LOGS_PATH

SEPARATOR = "|"
SLASH = "/"
DOT = "."

def registerSession(rows):
    logFile = open(LOGS_PATH,'w+')
    for row in rows:
        row = row.split(SEPARATOR)
        if(row[1] != 'P' and row[1] != 'start' and row[1] != 'end'):
            row[1] = 'P'
        processedRow = SEPARATOR.join(row)
        logFile.write(processedRow)
    logFile.close()
 
# def crearSesion(self):
#     sesiones =[] 
#     scores = []
#     if(t_juego!=[]):
#         user = self.getUser()
#         for r in roms:
#             rom = roms.pop() #Nombre Rom
#             ruta = rutaRoms.pop()
#             tiempo = t_juego.pop()
#             fecha = f_juego.pop()

#             roms.insert(0,rom)
#             rutaRoms.insert(0,ruta)
#             t_juego.insert(0,tiempo)
#             f_juego.insert(0,fecha)

#             datetimeobject = datetime.strptime(fecha, "%H:%M:%S %d/%m/%Y")
#             fecha = datetimeobject.strftime("%Y-%m-%d %H:%M:%S")
#             scores = self.getScores(ruta,rom)
#             #si hay mas de una puntuacion por sesion se duplican
#             for s in scores:
#                 tupla = (0,user,rom,fecha,tiempo,s)
#                 sesiones.insert(0,tupla)
#                 print(tupla)

#         return sesiones
#     else: print("La lista ya está procesada")

def getUser(self):
    user = "default"
    lector = nfc()
    db = datos()
    if(lector.leerNfc() != None):
        print(lector.id)
        try:
            db.connect()
            user = db.takeid(lector.id)
            db.close()
        except:
            print("No se puede conectar a la base de datos")
    return user

def getSession(rowSessions: list[str]):
    objSessions: list[object] = []
    for session in rowSessions:
        names: list[str] = session.split(SEPARATOR)
        state: str = names[1]
        gamePath: str = names[4]
        pathSections: str = gamePath.split(SLASH)
        gameFile = pathSections[len(pathSections)-1]
        gameName = gameFile.split(DOT)[0]

        if(state != 'P' and state != 'start' and state != 'end'):
            # Init Date
            stringDate = names[0]
            dateTime = datetime.strptime(stringDate, '%H:%M:%S %d/%m/%Y')
            initDate = dateTime.strftime('%Y-%m-%dT%H:%M:%S')

            # Score
            # TODO get the max score maybe ? 
            score = getScores(gamePath, gameName)

            # Duration
            stringDuration = names[1]
            dateTimeDuration = datetime.strptime(stringDuration, "%H:%M:%S") - datetime.strptime('00:00:00', "%H:%M:%S")
            duration = dateTimeDuration.total_seconds()

            # Game Id
            gameId = None
            try:
                data = login()
                token = data['access_token'] if data else None
                strapiGame = getGameBySlug(gameName, token) if token else None
                gameId = strapiGame['id'] if strapiGame else None
            except Exception as err:
                print(f'{error}',err)

            # Not implemented yet
            # Start the process of taking the nfc from the user

            # User Id
            # TODO read nfc and try to get auser if no use is found
            # we get a default user example: userId 1
            gameUserId = None
            try:
                data = login()
                token = data['access_token']
                # TODO change this obviously
                nfc = '1234'
                strapiGameUser = getPlayerByNfc(nfc, token)
                gameUserId = strapiGameUser['id']
            except Exception as err:
                print(f'{error}',err)

            newSession: object = {
                'initDate': initDate,
                'duration': int(duration),
                'score': int(max(score)),
                'gameId': gameId,
                'gameName': gameName,
                'userId': gameUserId,
            }
            objSessions.append(newSession)
    # TODO we always return the first but we should do something with it
    return objSessions[0] if len(objSessions) > 0 else None