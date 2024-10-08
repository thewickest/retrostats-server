import requests
from variables import API_URL, API_USER, API_PASSWORD

def login():
    user = {
        "username": API_USER,
        "password": API_PASSWORD
    }
    return requests.post(f'{API_URL}/auth/login', json=user)

def createSession(session: str, token: str):
    return requests.post(f'{API_URL}/sessions', json=session, 
                            headers={'Authorization': f'Bearer {token}'})
    

def getGameBySlug(gameName: str, token: str):
    return requests.get(f'{API_URL}/games/slug/{gameName}', 
                            headers={'Authorization': f'Bearer {token}'})

def getPlayerByNfc(nfc: str, token: str):
    return requests.get(f'{API_URL}/players/{nfc}', 
                            headers={'Authorization': f'Bearer {token}'})