import RPi.GPIO as GPIO
from time import sleep
import moteur
import canon

managMoteur = moteur.Moteurs(36, 22, 29, 31, 16, 37, 29, 31, 13, 15)
GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(36, GPIO.OUT)
# GPIO.setup(29,GPIO.OUT)
# GPIO.setup(31, GPIO.OUT)
# GPIO.output(29, GPIO.HIGH)
# GPIO.output(31, GPIO.LOW)
# pwmEnA = GPIO.PWM(36,100)
# pwmEnA.start(25)
coordsRotation = [400,400]
while(1) :
    print("test")
    
#     GPIO.output(5, GPIO.HIGH)
#     GPIO.output(6, GPIO.LOW)

#   
#     
GPIO.cleanup()