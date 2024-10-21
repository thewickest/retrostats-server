from constants import SEPARATOR, NEWLINE, error

def parser(textScorePath, byteScorePath):
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