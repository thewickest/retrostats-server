#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("ESPERANDO LECTURA....")
    id  = reader.read_id()
    print("LECTURA REALIZADA")
    print(id)
finally:
    GPIO.cleanup()
