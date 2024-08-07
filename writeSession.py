from datetime import datetime
from nfc import NFC as nfc
from dbFuncs import Datos as datos
from readScoress import ScoreReader as scoreReader
from pathlib import Path

#leo cada linea para coger el emulador y la ruta de la rom
c = "|"
b = "/"
log = False
roms = [] #zips
rutaRoms = []
rom = ""
rutaRom = ""
score = ""
t_juego = []
f_juego = []
home = str(Path.home())

class Sesion(object):
    def _init_(self):
        self.rom = rom
        self.rutaRom = rutaRom
        self.score = score
        self.t_juego = t_juego
        self.f_juego = f_juego

    def openlog(self):
        f = open(home+"/RetroStats/logs/game_stats.log","r")
        lines = f.readlines()
        f.close()
        return lines
    def procesar(self,lines):
        fw = open(home+"/RetroStats/logs/game_stats.log","w+")
        for l in lines:
            l = l.split(c)
            r = l[4].split(b)[6] #tengoq que quitar el espacio del principio, mirar como
            if(l[1]!="P" and l[1]!="start" and l[1]!="end"):
                rutaRoms.append(l[4].rstrip(r))
                roms.append(r) #nombre del zip extraido de la ruta
                t_juego.append(l[1])
                f_juego.append(l[0])
            e = c.join(l)
            fw.write(e)
        fw.close()
    def confirmarSesion(self,lines):
        fw = open(home+"/RetroStats/logs/game_stats.log","w+")
        for l in lines:
            l = l.split(c)
            if(l[1]!="P" and l[1]!="start" and l[1]!="end"):
                l[1]="P"
            e = c.join(l)
            fw.write(e)
        fw.close()    
    def crearSesion(self):
        sesiones =[] 
        scores = []
        if(t_juego!=[]):
            user = self.getUser()
            for r in roms:
                rom = roms.pop() #Nombre Rom
                ruta = rutaRoms.pop()
                tiempo = t_juego.pop()
                fecha = f_juego.pop()

                roms.insert(0,rom)
                rutaRoms.insert(0,ruta)
                t_juego.insert(0,tiempo)
                f_juego.insert(0,fecha)

                datetimeobject = datetime.strptime(fecha, "%H:%M:%S %d/%m/%Y")
                fecha = datetimeobject.strftime("%Y-%m-%d %H:%M:%S")
                scores = self.getScores(ruta,rom)
                #si hay mas de una puntuacion por sesion se duplican
                for s in scores:
                    tupla = (0,user,rom,fecha,tiempo,s)
                    sesiones.insert(0,tupla)
                    print(tupla)

            return sesiones
        else: print("La lista ya está procesada")
    def getUser(self):
        user = "default"
        lector = nfc()
        db = datos()
        if(lector.leerNfc() != None):
            print(lector.id)
            try:
                db.connect()
                user = db.takeid(lector.id)
                db.close()
            except:
                print("No se puede conectar a la base de datos")
        return user
    def getScores(self,ruta,rom):
        sr = scoreReader()
        return sr.getScores(ruta,rom)
        


        
