from datetime import datetime

# FORMATO DE FECHA /opt/retropie/config/all/runcomand-onstart.sh - ..onend.sh
DATE_FORMAT = "%H:%M:%S %d/%m/%Y"
SEPARATOR = "|"

# Returns the session date [initDate, endDate]
def getSessionDate(rows: list[str]):
    sessionDate: list[str] = []
    for row in rows:
        names = row.split(SEPARATOR)

        if names[1] == "start":
            sessionDate.append(names[0])
        
        if names[1] == "end":
            sessionDate.append(names[0])

    return sessionDate

# Returns the sessiontime endDate - initDate
def getSessionTime(sessionDate: list[str]) -> str:
    sessionTime: str = ''
    # TODO do a forloop
    if(len(sessionDate) > 0):
        sessionTime: datetime = datetime.strptime(sessionDate[1], DATE_FORMAT) - datetime.strptime(sessionDate[0], DATE_FORMAT)
    return str(sessionTime)