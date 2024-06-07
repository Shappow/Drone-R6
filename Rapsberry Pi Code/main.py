import RPi.GPIO as GPIO
from time import sleep
import moteur
import canon

managMoteur = moteur.Moteurs(7, 37, 31, 29, 15, 13, 26, 24, 40, 38)
managMoteur.reset_PWM()
# Avant gauche
# GPIO.setwarnings(False)                               
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(37, GPIO.OUT)
# GPIO.setup(40,GPIO.OUT)
# GPIO.setup(38, GPIO.OUT)
# GPIO.output(40, GPIO.LOW)                                                                                                                                                                                                                                                                                 
# GPIO.output(38, GPIO.LOW)
# # Arrière droite 
# GPIO.setup(13,GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)                                                                                                                                                                                                                                                                                                                                                                                                   
# GPIO.output(13, GPIO.LOW)                                                                                                                                                                                                                                                                                 
# GPIO.output(15, GPIO.LOW)
# # Arrière Gauche
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(31,GPIO.OUT)
# GPIO.setup(29, GPIO.OUT)                                                                                                                                                                                                                                                                                           
# GPIO.output(31, GPIO.LOW)                                                                                                                                                                                                                                                                     
# GPIO.output(29, GPIO.LOW)
# # Avant droite 
# GPIO.setup(26,GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)
# GPIO.output(24, GPIO.LOW)                                                                                                                                                                                                                                                                                 
# GPIO.output(26, GPIO.HIGH)
# pwmEnA = GPIO.PWM(7,50)
# pwmEnA.start(50)
# pwmEnA.ChangeDutyCycle(50)
# managMoteur.moveMotor("front","F1",50,False)
# managMoteur.moveMotor("back","B2",50,True)
# managMoteur.moveMotor("front","F2",50,True)
# managMoteur.moveMotor("back","B1",50,F)
coordsRotation = [50,50]
managMoteur.rotation(coordsRotation)
#coordsTranslation = [25,25]
#managMoteur.translation(coordsTranslation)
while True :
    x=0
    
#     GPIO.output(5, GPIO.HIGH)
#     GPIO.output(6, GPIO.LOW)

#   
#     
GPIO.cleanup()