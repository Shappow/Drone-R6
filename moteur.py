import RPi.GPIO as GPIO


class Moteurs : 
	
	"""
		  front
	+--+---------+--+	
	|\ |F1     F2| /|
	|\ |enA   enB| /|
	+--+		 +--+
	   |         |
	   |         |
	+--+		 +--+
	|/ |enB	  enA| \|
	|/ |B1	   B2| \|
	+--+---------+--+
		   back
	"""
	pinsBackMotors = {
		"enA" : -1,
		"enB" : -1,
		"in1" : -1,
		"in2" : -1,
		"in3" : -1,
		"in4" : -1
	}
	pinFrontMotors = {
		"enA" : -1,
		"enB" : -1,
		"in1" : -1,
		"in2" : -1,
		"in3" : -1,
		"in4" : -1
		
	}
	
	coordsTranslation = [0,0]
	coordsRotation = [0,0]
	pwmEnA = 0
	pwmEnB = 0
	
	MAXIMUM_PWM = 100
	
	# Constantes Translation
	MAX_XCOORDS_TRANS = 100
	MIN_XCOORDS_TRANS = 0
	
	MAX_YCOORDS_TRANS= 100
	MIN_YCOORDS_TRANS = 0
	
	# Constantes Rotation
	MAX_XCOORDS_ROT= 100
	MAX_YCOORDS_ROT = 100
	
	MIN_XCOORDS_ROT = 0
	MIN_YCOORDS_ROT = 0
	
	# Constantes Dead Point
	
	MAX_XCOORDS_DEAD = 60
	MIN_XCOORDS_DEAD = 40
	
	MAX_YCOORDS_DEAD= 60
	MIN_YCOORDS_DEAD = 40
	
	def __init__ (self, EnA, EnB, backIn1,backIn2,backIn3,backIn4,frontIn1,frontIn2,frontIn3,frontIn4) :
		self.pinBackMotors  = {
			"enA" : EnA,
			"enB" : EnB,
			"in1" : backIn1,
			"in2" : backIn2,
			"in3" : backIn3,
			"in4" : backIn4
		}
		
		self.pinFrontMotors  = {
			"enA" : EnA,
			"enB" : EnB,
			"in1" : frontIn1,
			"in2" : frontIn2,
			"in3" : frontIn3,
			"in4" : frontIn4
		} 
		GPIO.setmode(GPIO.BOARD)
		
		
		GPIO.setup(EnA,GPIO.OUT)
		GPIO.setup(EnB,GPIO.OUT)
		
		self.pwmEnA = GPIO.PWM(EnA,100)
		self.pwmEnB = GPIO.PWM(EnB,100)
		self.pwmEnA.start(0)
		self.pwmEnB.start(0)

		# Moteurs Front
		
		GPIO.setup(frontIn1,GPIO.OUT)
		GPIO.setup(frontIn2,GPIO.OUT)
		GPIO.setup(frontIn3,GPIO.OUT)
		GPIO.setup(frontIn4,GPIO.OUT)
		
		
		# Moteurs Back
		GPIO.setup(backIn1,GPIO.OUT)
		GPIO.setup(backIn2,GPIO.OUT)
		GPIO.setup(backIn3,GPIO.OUT)
		GPIO.setup(backIn4,GPIO.OUT)

		
		
	# side is "front" or "back"	
	# motor is the motor name (F1,F2,F3,F4)
	# direction 1 forward 0 backwards
	
	# TODO : vérifier les pins de direction
	def moveMotor(self, side, motor, speed, direction):
		if side == "front":
			if motor == "F1":
				if speed == 0:
					GPIO.output(self.pinFrontMotors["in1"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in2"], GPIO.LOW)
				elif direction:
					GPIO.output(self.pinFrontMotors["in1"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in2"], GPIO.HIGH)
				else:
					GPIO.output(self.pinFrontMotors["in2"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in1"], GPIO.HIGH)
				self.pwmEnA.ChangeDutyCycle(speed)
			elif motor == "F2":
				if speed == 0:
					GPIO.output(self.pinFrontMotors["in3"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in4"], GPIO.LOW)
				elif direction:
					GPIO.output(self.pinFrontMotors["in4"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in3"], GPIO.HIGH)
				else:
					GPIO.output(self.pinFrontMotors["in3"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in4"], GPIO.HIGH)
				self.pwmEnB.ChangeDutyCycle(speed)
			return
		elif side == "back":
			if motor == "B2":
				if speed == 0:
					GPIO.output(self.pinBackMotors["in1"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in2"], GPIO.LOW)
				elif direction:
					GPIO.output(self.pinBackMotors["in1"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in2"], GPIO.HIGH)
				else:
					GPIO.output(self.pinBackMotors["in2"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in1"], GPIO.HIGH)
				self.pwmEnA.ChangeDutyCycle(speed)
			elif motor == "B1":
				if speed == 0:
					GPIO.output(self.pinBackMotors["in3"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in4"], GPIO.LOW)
				if direction:
					GPIO.output(self.pinBackMotors["in3"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in4"], GPIO.HIGH)
				else:
					GPIO.output(self.pinBackMotors["in4"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in3"], GPIO.HIGH)
				self.pwmEnB.ChangeDutyCycle(speed)
			return
		else:
			print("error, no side found")
	# TODO : Définir pwm et range des coordonnées
	def rotation(self, coordsRotation) :
		coordsRotation[0] = min(max(coordsRotation[0], self.MIN_XCOORDS_ROT, self.MAX_XCOORDS_ROT))
                                
		if coordsRotation[0] < self.MAX_XCOORDS_DEAD and coordsRotation[0] > self.MIN_XCOORDS_DEAD :
			return
		# rotationClockWise 
		elif coordsRotation > 0 :
			moveMotor("front", "F1", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 0)
			moveMotor("front", "F2", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 0)
			moveMotor("back", "B3", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 1)
			moveMotor("back", "B4", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 1)
		elif coordsRotation < 0 :
			moveMotor("front", "F1", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 1)
			moveMotor("front", "F2", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 1)
			moveMotor("back", "B3", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 0)
			moveMotor("back", "B4", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , 0)
	
	# TODO : Définir pwm et range des coordonnées
	def translation(self, coordsTranslation) :
		coordsTranslation[0] = min(max(coordsTranslation[0], self.MIN_XCOORDS_TRANS, self.MAX_XCOORDS_TRANS))
		coordsTranslation[1] = min(max(coordsTranslation[1], self.MIN_YCOORDS_TRANS, self.MAX_YCOORDS_TRANS))
		# Dead Point
		if (coordsTranslation[0] < self.MAX_XCOORDS_DEAD)  and (coordsTranslation[0] > self.MIN_XCOORDS_DEAD) and (coordsTranslation[1] < self.MAX_YCOORDS_DEAD)  and (coordsTranslation[1] > self.MIN_YCOORDS_DEAD) :
			return
		
		# Avancée 
		elif (coordsTranslation[0] > self.MIN_XCOORDS_DEAD) and coordsTranslation[0] < self.MAX_XCOORDS_DEAD and coordsTranslation[1] > self.MAX_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_TRANS :
			moveMotor("front", "F1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , 0)
			moveMotor("front", "F2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , 1)
			moveMotor("back", "B1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , 1)
			moveMotor("back", "B2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM, 0)
		
		# Recul 
		elif coordsTranslation[0] > self.MIN_XCOORDS_DEAD  and coordsTranslation[0] < self.MAX_XCOORDS_DEAD and coordsTranslation[1] > self.MIN_YCOORDS_DEAD and coordsTranslation[1] < self.MIN_YCOORDS_TRANS :
			moveMotor("front", "F1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , 1)
			moveMotor("front", "F2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , 0)
			moveMotor("back", "B1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , 0)
			moveMotor("back", "B2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM, 1)
			
		
		# Translation droite 
		elif coordsTranslation[0] > self.MAX_XCOORDS_TRANS  and coordsTranslation[0] < self.MAX_XCOORDS_DEAD and coordsTranslation[1] > self.MIN_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_DEAD :
			moveMotor("front", "F1", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, 0)
			moveMotor("front", "F2", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, 1)
			moveMotor("back", "B1", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, 1)
			moveMotor("back", "B2", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, 0)
		
		# Translation gauche 
		elif coordsTranslation[0] > self.MIN_XCOORDS_TRANS  and coordsTranslation[0] < self.MIN_XCOORDS_DEAD and coordsTranslation[1] > self.MIN_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_DEAD :
			moveMotor("front", "F1", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM , 1)
			moveMotor("front", "F2", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM , 0)
			moveMotor("back", "B1", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, 0)
			moveMotor("back", "B2", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, 1)
			
		
		# Diagonale haut gauche 
		elif coordsTranslation[0] > self.MIN_XCOORDS_TRANS and coordsTranslation[0] < self.MIN_XCOORDS_DEAD  and coordsTranslation[1] > self.MAX_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_TRANS :
			moveMotor("front", "F1", (0 , 0))
			moveMotor("front", "F2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 0)
			moveMotor("back", "B1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 1)
			moveMotor("back", "B2", (0, 0))
			
		# Diagonale haut droite 
		elif coordsTranslation[0] > self.MAX_XCOORDS_DEAD  and coordsTranslation[0] < self.MAX_XCOORDS_TRANS and coordsTranslation[1] > self.MAX_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_TRANS :
			moveMotor("front", "F1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 0)
			moveMotor("front", "F2", (0, 0))
			moveMotor("back", "B1", (0, 1))
			moveMotor("back", "B2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 0)	
		
		# Diagonale bas gauche 
		elif coordsTranslation[0] > self.MIN_XCOORDS_TRANS and coordsTranslation[0] < self.MIN_XCOORDS_DEAD  and coordsTranslation[1] > self.MAX_YCOORDS_TRANS and coordsTranslation[1] < self.MIN_YCOORDS_DEAD :
			moveMotor("front", "F1", (0 , 0))
			moveMotor("front", "F2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 1)
			moveMotor("back", "B1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 0)
			moveMotor("back", "B2", (0, 0))
			
		# Diagonale bas droite 
		elif cocoordsTranslation[0] > self.MAX_XCOORDS_DEAD  and coordsTranslation[0] < self.MAX_XCOORDS_TRANS and coordsTranslation[1] > self.MAX_YCOORDS_TRANS and coordsTranslation[1] < self.MIN_YCOORDS_DEAD : 
			moveMotor("front", "F1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 1)
			moveMotor("front", "F2", (0, 0))
			moveMotor("back", "B1", (0, 1))
			moveMotor("back", "B2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, 1)	
		
		
