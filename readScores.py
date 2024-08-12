import filecmp 
from shutil import copyfile
from switcher import Switcher
from pathlib import Path
c = "|"
jump = '\n'
# rutaScores = "mame2003/hi/"

# partialScorePath =  "mame2003/hi/"
partialScorePath = 'data/'
home = str(Path.home())

def compareScoreFiles(nameGame):
    #se compara para saber si hay puntuaciones nuevas
    # fr = home+"/RetroStats/scores/"+nameGame+".txt"
    # fa = home+"/RetroStats/scores/"+nameGame+"B.txt"
    fr = ('./scores/%s.txt' % (nameGame))
    fa = ('./scores/%sB.txt' % (nameGame))

    #si las hay, se extrae el conjunto de lineaas distintas.
    scores = [0]
    try:
        comp = filecmp.cmp(fr,fa,shallow = False)
        if (not comp):
            file1 = open(fr,"r")
            file2 = open(fa,"r")
            scores = getDifference(file1,file2)
    finally:
        copyfile(fr,fa)
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
        print(lines)
    return lines

def processHiFiles(ruta,nameGame):
    sw = Switcher()
    sw.hiToText(ruta,nameGame)

def getScores(gamePath, nameGame):

    gamePath = gamePath.split("/")
    gamePath.pop()
    gamePath = ("/").join(gamePath)

    fullScorePath = gamePath + partialScorePath + nameGame + ".hi"

    # Converts the score files saved in bytes into text.
    # TODO maybe after this, we could delete the HI file to always save a score even if it's too low
    processHiFiles(fullScorePath, nameGame)

    # Return the scores if there is score differences
    return compareScoreFiles(nameGame)
