import filecmp
from pathlib import Path

rutaScoresMame2003 = "mame2003/hi/"
c = "|"
jump = "\n"
home = str(Path.home())
class Switcher(object):
    def hiToText(self,ruta,nombre):
        method_name = 'hiToText_' + str(nombre)
        method = getattr(self, method_name)  
        return method(ruta,nombre)
 
    def hiToText_pang(self,ruta,nombre):
        fw = open(home+"/RetroStats/scores/"+nombre+".txt","w+")
        with open(ruta+rutaScoresMame2003+nombre+".hi","rb") as f:
            byte = "empty"
            while byte:
                scores = []
                byte = f.read(3) #scores
                score = str(int(byte.hex())*10)
                scores.append(score)

                byte = f.read(3) #acronimo
                name = str(byte,"latin1")
                scores.append(name)

                byte = f.read(1) #stage
                scores.append(byte.hex())

                nothing = f.read(7) #orden
                byte = f.read(1).hex()
                if byte == '':  byte = "10"
                scores.append(byte)

                line = c.join(scores)
                fw.write(line+jump)

                byte = f.read(1)
        fw.close() 
    def hiToText_invaders(self,ruta,nombre):
        fw = open(home+"/RetroStats/scores/"+nombre+".txt","w+")
        with open(ruta+rutaScoresMame2003+nombre+".hi","rb") as f:
            byte = f.read(1)
            low = byte.hex()
            byte = f.read(1)
            hi = byte.hex()
            
            score = str(hi)+str(low)
            fw.write(score)
            print(score)
        fw.close() 
    def hiToText_mspacman(self,ruta,nombre):
        print("no hago nada")
    def hiToText_mslug(self,ruta,nombre):
        print("no hago nada")