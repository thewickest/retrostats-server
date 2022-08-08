#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

class NFC(object):
    id = "default"
    def _init_(self):
        self.id = id

    def leerNfc(self):
        try:
            print("ESPERANDO LECTURA....")
            id = reader.read_id_no_block()
            time.sleep(1)
            if(id!=None):
                self.id = id
            return id
        finally:
            print("LECTURA REALIZADA")
            GPIO.cleanup()