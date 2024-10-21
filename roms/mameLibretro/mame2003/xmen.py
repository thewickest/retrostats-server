from constants import SEPARATOR, NEWLINE, error

def parser(textScorePath, byteScorePath):
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