from readTimes import getSessionDate, getSessionTime
from writeSession import getSession, registerSession
from files import openLogFile, writeLogFile
from variables import LOGS_PATH
from api.api import createSession, login
from requests import ConnectionError
from constants import info, error, warn
from readScores import resetScores
import requests
from dbfuncs import Database

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
        print('something')
        print(err)

    # Generate the sessions
    sessions: list[object] = []
    if(token):
        sessions: list[object] = getSession(rows, token)

    if(len(sessions) > 0 and token):
        ## save sesssion in local database
        # try:
        #     database = Database()
        #     database.connect()
        # except:
        #     print('cant connect')

        # save session in api
        try:
            for session in sessions:
                response = createSession(session, token)
                response.raise_for_status()
                strapiSession = response.json()
                print(f'{info} Session created succesfully')
                print(f'{info}', strapiSession)

            ## TODO instead of copying the file, we can register the score inside
            ## a database
            # copyScoreFile(session['gameName'])
            # NOTE each time a player starts a new game, the byte scores are new,
            # that means that he/she does not need to have a high score to save the
            # score into the system. Just the minimum
        except ConnectionError as err:
            print(f'{error} There was some error connecting to the API. Probably is down')
            # TODO make something like this
            # registerSession(rows, 'Error')
        except requests.exceptions.HTTPError as err:
            print(f'{error}', err)
            print(f'{error}', response.json())
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

if __name__ == "__main__":
    main()