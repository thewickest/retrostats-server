SEPARATOR = "|"

# Read the log file
def openLogFile(logPath: str) -> list[str]:
    logFile = open(logPath,"r")
    rows: list[str] = logFile.readlines()
    logFile.close()
    return rows

# Write log file
def writeLogFile(logPath: str, sessionDate: list[str], sessionTime: str):

    # TODO probably we can do it better
    # Read the file
    logFile = open(logPath,"r")
    newLines: list[str] = []

    for line in logFile:
        session: str = ''
        names: list[str] = line.split(SEPARATOR)

        if names[0] == sessionDate[0]: # is an start date
            names[1] = sessionTime
            session = SEPARATOR.join(names)
        elif names[0] == sessionDate[1]: # is and end date
            session = ''
        elif names[1] != 'start' and names[1] != 'end':
            session = SEPARATOR.join(names)
        
        newLines.append(session)

    logFile.close()

    # Write in the file
    logFile = open(logPath, 'w+')
    logFile.writelines(newLines)
    logFile.close()