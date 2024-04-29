import RPi.GPIO as GPIO


class Moteurs : 
	
	pinsBackMotors = {
		enA : -1,
		enB : -1,
		in1 : -1,
		in2 : -1,
		in3 : -1,
		in4 : -1
	}
	pinFrontMotors = {
		enA : -1,
		enB : -1,
		in1 : -1,
		in2 : -1,
		in3 : -1,
		in4 : -1
		
	}
	
	coordsTranslation = [0,0]
	coordsRotation = [0,0]
	
	
	def __init__ (self, backEnA, backEnB, backIn1,backIn2,backIn3,backIn4,frontEnA, frontEnB, frontIn1,frontIn2,frontIn3,frontIn4) :
		pinBackMotors  = {
			enA : backEnA,
			enB : backEnB,
			in1 : backIn1,
			in2 : backIn2,
			in3 : backIn3,
			in4 : backIn4
		} 
		pinfrontMotors  = {
			enA : frontEnA,
			enB : frontEnB,
			in1 : frontIn1,
			in2 : frontIn2,
			in3 : frontIn3,
			in4 : frontIn4
		} 
		GPIO.setmode(GPIO.BOARD)
		
		GPIO.setup(backEnA,GPIO.OUT)
		GPIO.setup(backEnB,GPIO.OUT)
		GPIO.setup(backIn1,GPIO.OUT)
		GPIO.setup(backIn2,GPIO.OUT)
		GPIO.setup(backIn3,GPIO.OUT)
		GPIO.setup(backIn4,GPIO.OUT)
		
		GPIO.setup(frontEnA,GPIO.OUT)
		GPIO.setup(frontEnB,GPIO.OUT)
		GPIO.setup(frontIn1,GPIO.OUT)
		GPIO.setup(frontIn2,GPIO.OUT)
		GPIO.setup(frontIn3,GPIO.OUT)
		GPIO.setup(frontIn4,GPIO.OUT)
	
	# side is "front" or "back"	
	# direction 1 forward 0 backwards
	
	# TODO : vérifier les pins de direction
	def moveMotor(side, en, speed, direction)
		if "back" : 
			if en = "enA" :
				pwm = GPIO.PWM(pinBackMotors["enA"], 60)
				if direction : 
					GPIO.output(pinBackMotors["in1", GPIO.LOW)
					GPIO.output(pinBackMotors["in2", GPIO.HIGH)
				else : 
					GPIO.output(pinBackMotors["in2", GPIO.LOW)
					GPIO.output(pinBackMotors["in1", GPIO.HIGH)
			elif en = "enB" :
				pwm = GPIO.PWM(pinBackMotors["enB"], 60)
				if direction : 
					GPIO.output(pinBackMotors["in3", GPIO.LOW)
					GPIO.output(pinBackMotors["in4", GPIO.HIGH)
				else : 
					GPIO.output(pinBackMotors["in4", GPIO.LOW)
					GPIO.output(pinBackMotors["in3", GPIO.HIGH)
			pwm.start(speed)
			return 
		elif "front" : 
			if en = "enA" :
				pwm = GPIO.PWM(pinFrontMotors["enA"], 60)
				if direction : 
					GPIO.output(pinFrontMotors["in1", GPIO.LOW)
					GPIO.output(pinFrontMotors["in2", GPIO.HIGH)
				else : 
					GPIO.output(pinFrontMotors["in2", GPIO.LOW)
					GPIO.output(pinFrontMotors["in1", GPIO.HIGH)
			elif en = "enB" :
				pwm = GPIO.PWM(pinFrontMotors["enB"], 60)
				if direction : 
					GPIO.output(pinFrontMotors["in3", GPIO.LOW)
					GPIO.output(pinFrontMotors["in4", GPIO.HIGH)
				else : 
					GPIO.output(pinFrontMotors["in4", GPIO.LOW)
					GPIO.output(pinFrontMotors["in3", GPIO.HIGH)
			pwm.start(speed)
			return
		else : 
			print ("error, no side found")
	
	# TODO : Définir pwm et range des coordonnées
	def rotation(coordsRotation)
		if (motor) 
