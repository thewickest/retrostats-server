from constants import SEPARATOR, NEWLINE, error

def parser(textScorePath, byteScorePath):
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