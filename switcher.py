from pathlib import Path
from constants import error

c = "|"
jump = "\n"
home = str(Path.home())

class Switcher(object):
    def hiToText(self, textScorePath, byteScorePath, gameName):
        methodName = 'hiToText_' + str(gameName)
        # Calls the
        method = getattr(self, methodName)
        return method(textScorePath, byteScorePath)
 
    def hiToText_pang(self, textScorePath, byteScorePath):
        try:
            fw = open(textScorePath,"w+")
            with open(byteScorePath,"rb") as f:
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
        except Exception as err:
            print(f'{error}', err)
    def hiToText_invaders(self, textScorePath, byteScorePath):
        try:
            fw = open(textScorePath,"w+")
            with open(byteScorePath,"rb") as f:
                byte = f.read(1)
                low = byte.hex()
                byte = f.read(1)
                hi = byte.hex()
                
                score = str(hi)+str(low)
                fw.write(score)
            fw.close() 
        except Exception as err:
            print(f'{error}', err)
    def hiToText_mspacman(self, textScorePath, byteScorePath):
        try:
            fw = open(textScorePath,"w+")
            with open(byteScorePath,"rb") as f:
                byte = f.read(1)
                low = byte.hex()
                byte = f.read(1)
                hi = byte.hex()
                
                score = str(hi)+str(low)
                fw.write(score)
            fw.close()
        except Exception as err:
            print(f'{error}', err)
    def hiToText_pacman(self, textScorePath, byteScorePath):
        try:
            fw = open(textScorePath,"w+")
            with open(byteScorePath,"rb") as f:
                byte = f.read(1)
                low = byte.hex()
                byte = f.read(1)
                hi = byte.hex()
                
                score = str(hi)+str(low)
                fw.write(score)
            fw.close()
        except Exception as err:
            print(f'{error}', err)
    def hiToText_mslug2(self, textScorePath, byteScorePath):
        try:
            fw = open(textScorePath,"w+")
            with open(byteScorePath,"rb") as f:
                byte = 'empty'
                while byte:
                    scores = []
                    byte = f.read(1)
                    nothing = byte.hex()

                    # print(position)
                    # scores.append(position)

                    byte = f.read(3)
                    score = byte.hex()
                    scores.append(score)

                    byte = f.read(3)
                    name = str(byte,"latin1")
                    scores.append(name)

                    byte = f.read(1)
                    # nothing = byte.hex()
                    # scores.append(nothing)

                    byte = f.read(1)
                    state = byte.hex()
                    scores.append(state)

                    byte = f.read(1)
                    other = byte.hex()
                    scores.append(other)

                    # byte = f.read(3)

                    line = c.join(scores)
                    fw.write(line+jump)
            fw.close()
        except Exception as err:
            print(f'{error}', err)