import RPi.GPIO as GPIO

class Canon :
    
    servoBase = {
        "pin" : -1
        "angle" : 0
        }
    servoCanon = {
        "pin" : -1
        "angle" : 0
        }
    pwmBase = 0
    pwmCanon = 0
    MAX_SERVO_PWM = 1024
    MAX_ANGLE = 180
    
    def __init__(self, pinBase, pinCanon):
        servoBase["pin"] = pinBase
        servoCanon["angle"] = pinCanon
        GPIO.setmode(GPIO.BOARD)
		
		GPIO.setup(pinBase,GPIO.OUT)
		GPIO.setup(pinCanon,GPIO.OUT)
		
		pwmBase = GPIO.PWM(pinBase,GPIO.OUT)
		pwmCanon = GPIO.PWM(pinCanon,GPIO.OUT)
        
    def angleToPWM (self, angle):
        angle =  min(max(angle, 0, MAX_ANGLE))
        return angle/MAX_ANGLE * MAX_SERVO_PWM
    
    def moveServoBase (angle) :
        pwmBase.start(angleToPWM(angle))
    
    def moveServoCanon (angle) :
        pwmCanon.start(angleToPWM(angle))
        
        
    
    


