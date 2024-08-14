import requests
from variables import API_URL, API_USER, API_PASSWORD

def login():
    user = {
        "username": API_USER,
        "password": API_PASSWORD
    }
    response = requests.post(f'{API_URL}/auth/login', json=user)
    return response.json()

def createSession(session: str, token: str):
    response = requests.post(f'{API_URL}/sessions', json=session, 
                             headers={'Authorization': f'Bearer {token}'})
    return response.json()

def getGameBySlug(gameName: str, token: str):
    # response = requests.get(f'{API_URL}/game/slug/{gameName}', 
    #                         headers={'Authorization': f'Bearer {token}'})
    # return response.json()
    return { 'id': 1, 'name': 'pang'}