import requests

url = 'http://localhost:3001/sessions'
token= 'Bearer almost'

def createSession(session):
    response = requests.post(url, json=session, headers={"Authorization": token})
    print(response.json())

def getAPISessions():
    response = requests.get(url)
    print(response.json())