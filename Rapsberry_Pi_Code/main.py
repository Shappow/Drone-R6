import RPi.GPIO as GPIO
from time import sleep
import moteur
import canon
import os
managMoteur = moteur.Moteurs(7, 37, 31, 29, 15, 13, 26, 24, 40, 38)
os.system('python3 video_stream.py')
while True :
    x=0
    
GPIO.cleanup()