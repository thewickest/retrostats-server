import filecmp 
from shutil import copyfile
from switcher import Switcher
from variables import TEXT_SCORES_PATH, BYTE_SCORES_PATH, ENV
from constants import error
from files import deleteFile

c = "|"
jump = '\n'

# TODO find a way to change this

def copyScoreFile(slug):
    currentFileScore = (TEXT_SCORES_PATH+'/%s.txt' % (slug))
    previousFileScore = (TEXT_SCORES_PATH+'/%sB.txt' % (slug))
    copyfile(currentFileScore, previousFileScore)

def resetScores(sessions):
    for session in sessions:
        slug = session['gameName']
        emulator = session['gameEmulator']
        gamePath = session['gamePath']
        textScoreFile = (TEXT_SCORES_PATH+'/%s.txt' % (slug))

        scorePath = gamePath + '/' + emulator + '/hi'
        if (ENV == 'local'):
            scorePath = BYTE_SCORES_PATH
        byteScoreFile = scorePath +'/'+ slug + ".hi"

        deleteFile(textScoreFile)
        deleteFile(byteScoreFile)

def compareScoreFiles(nameGame):
    currentPath = (TEXT_SCORES_PATH+'/%s.txt' % (nameGame))
    previousPath = (TEXT_SCORES_PATH+'/%s-base.txt' % (nameGame))

    scores = [0]
    try:
        comp = filecmp.cmp(currentPath, previousPath, shallow = False)
        if (not comp):
            currentFile = open(currentPath,"r+")
            previousFile = open(previousPath,"r+")
            scores = getDifference(currentFile, previousFile)
            # print('scores', scores)
    except Exception as err:
        print(f'{error}', err)
    finally:
        return scores

def getDifference(file1,file2):
    lines = []
    f1 = file1.readlines()
    f2 = file2.readlines()
    for f in f1:
        flag = True
        lf = f.split(c)
        for h in f2:
            lh = h.split(c)
            if (lf[0] == lh[0] and lf[1] == lh[1] and lf[2] == lh[2]):
                flag = False
                break
        if (flag==True):
            lines.insert(0,lf[0])
    return lines

def processHiFiles(textScorePath, byteScoresPath,nameGame):
    sw = Switcher()
    sw.hiToText(textScorePath, byteScoresPath, nameGame)

def getScores(gamePath, gameName, gameEmulator):

    gamePath = gamePath.split("/")
    gamePath.pop()
    gamePath = ("/").join(gamePath)

    scorePath = gamePath + '/' + gameEmulator + '/hi'
    if (ENV == 'local'):
        scorePath = BYTE_SCORES_PATH

    byteScorePath = scorePath +'/'+ gameName + ".hi"
    textScorePath = TEXT_SCORES_PATH +'/'+ gameName + '.txt'


    # Converts the score files saved in bytes into text.
    processHiFiles(textScorePath, byteScorePath, gameName)

    return compareScoreFiles(gameName)
