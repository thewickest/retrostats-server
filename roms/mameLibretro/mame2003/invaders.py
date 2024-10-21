from constants import error

def parser(textScorePath, byteScorePath):
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