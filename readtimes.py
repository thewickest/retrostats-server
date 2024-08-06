from datetime import datetime
from pathlib import Path

#FORMATO DE FECHA /opt/retropie/config/all/runcomand-onstart.sh - ..onend.sh
DATE_FORMAT = "%H:%M:%S %d/%m/%Y"

horainicio = []
horafinal = []
horasum = []
nombres = []
c = "|"
home = str(Path.home())
class Times(object):
    def _init_(self):
        self.horainicio = horainicio
        self.horafinal = horafinal
        self.horasum = horasum
        self.nombres = nombres
#metodo que abre y devuelve las lineas de un archivo
    def openlog(self):    
        f = open(home+"/RetroStats/logs/game_stats.log","r")
        rows = f.readlines()
        f.close()
        return rows

#metodo que devuelve las horas de inicio de las sesiones
    def process(self,rows):
        for row in rows:
            names = row.split(c)
            nombres.append(names)

            #crear structura de datos
            if names[1] == "end":
                horafinal.append(names[0])

            elif names[1] == "start":
                horainicio.append(names[0])
                horasum.append(names)
        return horainicio
        

#restar horaInicio y final para obtener el total de horas jugadas
    def sumarhoras(self, horainicio):
        for horas in horainicio:

            horai = horainicio.pop()
            horaf = horafinal.pop() #tengo que meterlo otra vez para que el bucle no acabe

            horainicio.insert(0,horai)
            horafinal.insert(0,horaf)

            horatotal= datetime.strptime(horaf,DATE_FORMAT) - datetime.strptime(horai,DATE_FORMAT)
            
            j= horasum.pop() #AQUI PASA ALGO QUE HACE QUE LA LISTA "NOMBRES" CAMBIE
            j[1] = str(horatotal)
            horasum.insert(0,c.join(j))

#COMIENZA LA ESCRITURA EN EL FICHERO
    def writelog(self):
        nf = open(home+"/RetroStats/logs/game_stats.log","w+")
        for m in nombres:
            if m[1] != 'end' and m[1] != 'start':
                j = c.join(m)
                nf.write(j)
        nf.close()