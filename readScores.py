import filecmp 
from shutil import copyfile
from switcher import Switcher
from pathlib import Path
from variables import TEXT_SCORES_PATH, BYTE_SCORES_PATH, ENV
from constants import error

c = "|"
jump = '\n'

# TODO find a way to change this
partialScorePath =  "/mame2003/hi"

def copyScoreFile(slug):
    currentFileScore = (TEXT_SCORES_PATH+'/%s.txt' % (slug))
    previousFileScore = (TEXT_SCORES_PATH+'/%sB.txt' % (slug))
    copyfile(currentFileScore, previousFileScore)


def compareScoreFiles(nameGame):
    # TODO the first time doesnt compare anything because there is no scoreTxt file
    #se compara para saber si hay puntuaciones nuevas
    fr = (TEXT_SCORES_PATH+'/%s.txt' % (nameGame))
    fa = (TEXT_SCORES_PATH+'/%sB.txt' % (nameGame))

    #si las hay, se extrae el conjunto de lineaas distintas.
    scores = [0]
    try:
        comp = filecmp.cmp(fr,fa,shallow = False)
        if (not comp):
            file1 = open(fr,"r+")
            file2 = open(fa,"r+")
            scores = getDifference(file1,file2)
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

def getScores(gamePath, gameName):

    gamePath = gamePath.split("/")
    gamePath.pop()
    gamePath = ("/").join(gamePath)

    scorePath = gamePath + partialScorePath
    if (ENV == 'local'):
        scorePath = BYTE_SCORES_PATH

    byteScorePath = scorePath +'/'+ gameName + ".hi"
    textScorePath = TEXT_SCORES_PATH +'/'+ gameName + '.txt'


    # Converts the score files saved in bytes into text.
    # TODO maybe after this, we could delete the HI file to always save a score even if it's too low
    processHiFiles(textScorePath, byteScorePath, gameName)

    # Return the scores if there is score differences
    return compareScoreFiles(gameName)
