from constants import error, NEWLINE, SEPARATOR

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

                    line = SEPARATOR.join(scores)
                    fw.write(line+NEWLINE)

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

                    byte = f.read(3)
                    score = byte.hex()
                    scores.append(score)

                    byte = f.read(3)
                    name = str(byte,"latin1")
                    scores.append(name)

                    byte = f.read(1)

                    byte = f.read(1)
                    state = byte.hex()
                    scores.append(state)

                    byte = f.read(1)
                    other = byte.hex()
                    scores.append(other)

                    line = SEPARATOR.join(scores)
                    fw.write(line+NEWLINE)
            fw.close()
        except Exception as err:
            print(f'{error}', err)

    def hiToText_xmen(self, textScorePath, byteScorePath):
        try:
            fw = open(textScorePath,"w+")
            with open(byteScorePath,"rb") as f:
                byte = "empty"
                characters = ['CYCLOPS', 'COLOSSUS', 'WOLVERINE', 'STORM', 'NIGHT CRAWLER', 'DAZZLER', '']
                count = 0
                character = characters[0]
                while byte:
                    scores = []
                    byte = f.read(1) # stage
                    stage = str(byte.hex())

                    byte = f.read(3)
                    name = ''.join(chr(b + ord('A')) for b in byte)

                    byte = f.read(2) # scores
                    score = str(byte.hex())
                    if count % 10 == 0:
                        character = characters[int(count/10)]
                    scores.append(score)
                    scores.append(name)
                    scores.append(stage)
                    scores.append(character)

                    line = SEPARATOR.join(scores)
                    fw.write(line+NEWLINE)

                    count += 1
            fw.close()
        except Exception as err:
            print(f'{error}', err)