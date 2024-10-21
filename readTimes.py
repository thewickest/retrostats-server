from datetime import datetime
from constants import DATE_FORMAT, SEPARATOR

# FORMATO DE FECHA /opt/retropie/config/all/runcomand-onstart.sh - ..onend.sh

# Returns the session date [initDate, endDate]
def getSessionDate(rows: list[str]) -> list[str]:
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
    if len(sessionDate) >= 2:
        try:
            # Parse the start and end dates using the provided date format.
            start_date = datetime.strptime(sessionDate[0], DATE_FORMAT)
            end_date = datetime.strptime(sessionDate[1], DATE_FORMAT)
            # Calculate the difference.
            if(end_date > start_date):
                sessionTime = end_date - start_date
            else:
                sessionTime = datetime.min.time()
        except ValueError:
            # Raise a ValueError if the date format is incorrect.
            raise ValueError("Dates must be in 'HH:MM:SS DD/MM/YYYY' format.")
    return str(sessionTime)