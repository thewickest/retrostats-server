from readTimes import getSessionDate, getSessionTime
from writeSession import getSession, registerSession
from files import openLogFile, writeLogFile
from variables import LOGS_PATH
from api.api import createSession, login
from requests import ConnectionError
from constants import info, error

def main():

    # Process logs file
    rows: list[str] = openLogFile(LOGS_PATH)
    print(f'{info} Procesando las horas...')
    sessionDates: list[str] = getSessionDate(rows)
    print(f'{info} Sumando las horas de las sesiones....')
    sessionTime: str = getSessionTime(sessionDates)
    if(len(sessionDates)):
        writeLogFile(LOGS_PATH, sessionDates, sessionTime)

    rows: list[str] = openLogFile(LOGS_PATH)
    print(f'{info} Procesando las sesiones...')
    # TODO: add proper type
    session: object = getSession(rows)

    # TODO add error handlers if 401
    if(session):
        try:
            data = login()
            token = data["access_token"]
            strapiSession = createSession(session, token)
            print(f'{info} Session created succesfully')
            print(f'{info}', strapiSession)
            registerSession(rows)
        except ConnectionError as err:
            print(f'{error} There was some error connecting to the API. Probably is down')
    else:
        print(f'{info} No session to register')

if __name__ == "__main__":
    main()