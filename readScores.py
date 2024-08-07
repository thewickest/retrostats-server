import filecmp 
from shutil import copyfile
from switcher import Switcher
from pathlib import Path
c = "|"
jump = '\n'
rutaScores = "mame2003/hi/"
home = str(Path.home())
class ScoreReader(object):

    def compareScoreFiles(self,nameGame):
        #se compara para saber si hay puntuaciones nuevas
        fr = home+"/RetroStats/scores/"+nameGame+".txt"
        fa = home+"/RetroStats/scores/"+nameGame+"B.txt"

        #si las hay, se extrae el conjunto de lineaas distintas.
        scores = [0]
        try:
            comp = filecmp.cmp(fr,fa,shallow = False)
            if (not comp):
                file1 = open(fr,"r")
                file2 = open(fa,"r")
                scores = self.getDifference(file1,file2)
                print(scores)
        finally:
            copyfile(fr,fa)
            return scores

    def getDifference(self,file1,file2):
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

    def processHiFiles(self,ruta,nameGame):
        sw = Switcher()
        sw.hiToText(ruta,nameGame)

    def getScores(self,ruta,rom):
        nameGame = rom.rstrip('.zip')
        self.processHiFiles(ruta,nameGame)
        return self.compareScoreFiles(nameGame)
