from readTimes import getSessionDate, getSessionTime
from writeSession import getSession, registerSession
from files import openLogFile, writeLogFile
from variables import LOGS_PATH
from api.api import createSession, login
from requests import ConnectionError
from constants import info, error, warn, PROCESSED, ERROR, CREATED
from readScores import resetScores
import requests
from dbfuncs import Database

def main():

    # Process logs file
    rows: list[str] = openLogFile(LOGS_PATH)
    print(f'{info} Processing time...')
    sessionDates: list[str] = getSessionDate(rows)
    print(f'{info} Adding hours to the sessions....')
    sessionTime: str = getSessionTime(sessionDates)
    if(len(sessionDates)):
        writeLogFile(LOGS_PATH, sessionDates, sessionTime)

    rows: list[str] = openLogFile(LOGS_PATH)
    print(f'{info} Processing the sessions...')

    # Login into the API to get the Access token
    token = None
    try:
        response = login()
        response.raise_for_status()
        data = response.json()
        token = data['access_token'] if data else None
    except ConnectionError:
        print(f'{error} Unable to login into the API. The API is down.')
    except requests.exceptions.HTTPError as err:
        if(err.response.status_code == 401):
            print(f'{error} Unauthorized user!')
    except Exception as err:
        print(f'{error} Unexpected error!')

    # Generate the sessions
    # Here we can check for previous sessions with status ERROR and return them
    sessions: list[object] = getSession(rows, token)

    # Connect to local database
    database = None
    try:
        database = Database()
        database.connect()
    except: 
        print('Cant connect to local database')
    
    backupSessions = []
    if(database):
        # save sesssions in local database
        try:
            backupSessions = database.insertSessions(sessions)
            errorSessions = database.getErrorSessions()
            backupSessions = backupSessions + errorSessions
        except Exception as err:
            print('An error ocurred while inserting the Sessions into the database')

    if(len(backupSessions) > 0 and database):

        # save session in api
        try:
            for session in backupSessions:
                response = createSession(session['session'], token)
                response.raise_for_status()
                strapiSession = response.json()
                print(f'{info} Session created succesfully')
                print(f'{info}', strapiSession)

                database.updateSessions(backupSessions, PROCESSED)

            ## TODO instead of copying the file, we can register the score inside
            ## a database
            # copyScoreFile(session['gameName'])
            # updateSession(id, 'PROCESSED')
            # NOTE each time a player starts a new game, the byte scores are new,
            # that means that he/she does not need to have a high score to save the
            # score into the system. Just the minimum
        except ConnectionError as err:
            print(f'{error} There was some error connecting to the API. Probably is down')
            database.updateSessions(backupSessions, ERROR)
        except requests.exceptions.HTTPError as err:
            print(f'{error}', err)
            print(f'{error}', response.json())
            database.updateSessions(backupSessions, ERROR)
    else:
        print(f'{warn} No sessions to register')

    # even if the creation of the session goes wrong, we reset the state of the scores to make sure that the next session
    # doesn't conflict with the new ones.
    # This is because we don't have any way to determine which score belongs to which session if there is a many to many relation.
    try:
        registerSession(rows)
        resetScores(sessions)
    except Exception as err:
        print(f'{error} There was an error while reseting the scores')
        print(f'{error}', err)

    database.close()

if __name__ == "__main__":
    main()