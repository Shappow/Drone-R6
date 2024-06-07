import RPi.GPIO as GPIO


class Moteurs : 
	
	"""
	This comment shows how the motors pins are seperated in the code.
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
	
	MAXIMUM_PWM = 50
	
	# Constantes Translation
	MAX_XCOORDS_TRANS = 50
	MIN_XCOORDS_TRANS = -50
	
	MAX_YCOORDS_TRANS= 50
	MIN_YCOORDS_TRANS = -50
	
	# Constantes Rotation
	MAX_XCOORDS_ROT= 50
	MAX_YCOORDS_ROT = 50
	
	MIN_XCOORDS_ROT = -50
	MIN_YCOORDS_ROT = -50
	
	# Constantes Dead Point
	
	MAX_XCOORDS_DEAD = 20
	MIN_XCOORDS_DEAD = -20
	
	MAX_YCOORDS_DEAD= 20
	MIN_YCOORDS_DEAD = -20
	
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
		GPIO.setmode(GPIO.BCM)
		
		
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


	def reset_PWM (self):
		GPIO.output(self.pinFrontMotors["in1"], GPIO.LOW)
		GPIO.output(self.pinFrontMotors["in2"], GPIO.LOW)
		GPIO.output(self.pinBackMotors["in1"], GPIO.LOW)
		GPIO.output(self.pinBackMotors["in2"], GPIO.LOW)
		GPIO.output(self.pinFrontMotors["in3"], GPIO.LOW)
		GPIO.output(self.pinFrontMotors["in4"], GPIO.LOW)
		GPIO.output(self.pinBackMotors["in3"], GPIO.LOW)
		GPIO.output(self.pinBackMotors["in4"], GPIO.LOW)
		self.pwmEnA.ChangeDutyCycle(0)
		self.pwmEnB.ChangeDutyCycle(0)
	
	# side is either "front" or "back"	
	# motor is the motor name (F1,F2,F3,F4)
	# isClockWise == true clock wise else its counter clockwise
	
	def moveMotor(self, side, motor, speed, isForward):
		if side == "front":
			if motor == "F1":
				if speed == 0:
					GPIO.output(self.pinFrontMotors["in1"], GPIO.LOW)
					GPIO.output(self.pinFrontMotors["in2"], GPIO.LOW)
				elif isForward == True:
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
				elif isForward == True:
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
				elif isForward == True:
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
				if isForward == True:
					GPIO.output(self.pinBackMotors["in3"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in4"], GPIO.HIGH)
				else:
					GPIO.output(self.pinBackMotors["in4"], GPIO.LOW)
					GPIO.output(self.pinBackMotors["in3"], GPIO.HIGH)
				self.pwmEnB.ChangeDutyCycle(speed)
			return
		else:
			print("error, no side found")
			
	# coordsRotation is a table of lenght 2
	def rotation(self, coordsRotation) :
		if coordsRotation[0] >= self.MAX_XCOORDS_ROT :
			coordsRotation[0] = self.MAX_XCOORDS_ROT
		elif coordsRotation[0] <= self.MIN_XCOORDS_ROT :
			coordsRotation[0] = self.MIN_XCOORDS_ROT
             
		if coordsRotation[0] < self.MAX_XCOORDS_DEAD and coordsRotation[0] > self.MIN_XCOORDS_DEAD :
			return
		# rotationClockWise 
		elif coordsRotation[0] > self.MAX_XCOORDS_ROT/2 :
			self.moveMotor("front", "F1", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , True)
			self.moveMotor("front", "F2", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , False)
			self.moveMotor("back", "B1", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , True)
			self.moveMotor("back", "B2", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , False)
		elif coordsRotation[0] < self.MAX_XCOORDS_ROT/2 :
			self.moveMotor("front", "F1", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , True)
			self.moveMotor("front", "F2", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , False)
			self.moveMotor("back", "B1", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , True)
			self.moveMotor("back", "B2", (abs(coordsRotation[0])/self.MAX_XCOORDS_ROT) * self.MAXIMUM_PWM , False)
	
	#  coordsTranslation is a table of length 2
	def translation(self, coordsTranslation) :
		if coordsTranslation[0] >= self.MAX_XCOORDS_TRANS :        
			coordsTranslation[0] = self.MAX_XCOORDS_TRANS
		elif coordsTranslation[0] <= self.MIN_XCOORDS_TRANS :
			coordsTranslation[0] = self.MIN_XCOORDS_TRANS
			
		if coordsTranslation[1] >= self.MAX_YCOORDS_TRANS :
			coordsTranslation[1] = self.MAX_YCOORDS_TRANS
		elif coordsTranslation[1] <= self.MIN_YCOORDS_TRANS :
			coordsTranslation[1] = self.MIN_YCOORDS_TRANS

		# Dead Point
		if (coordsTranslation[0] < self.MAX_XCOORDS_DEAD)  and (coordsTranslation[0] > self.MIN_XCOORDS_DEAD) and (coordsTranslation[1] < self.MAX_YCOORDS_DEAD)  and (coordsTranslation[1] > self.MIN_YCOORDS_DEAD) :
			return
		
		# Avancée 
		elif (coordsTranslation[0] > self.MIN_XCOORDS_DEAD) and coordsTranslation[0] < self.MAX_XCOORDS_DEAD and coordsTranslation[1] > self.MAX_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_TRANS :
			self.moveMotor("front", "F1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , True)
			self.moveMotor("front", "F2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , True)
			self.moveMotor("back", "B1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , True)
			self.moveMotor("back", "B2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM, True)
		
		# Recul 
		elif coordsTranslation[0] > self.MIN_XCOORDS_DEAD  and coordsTranslation[0] < self.MAX_XCOORDS_DEAD and coordsTranslation[1] < self.MIN_YCOORDS_DEAD and coordsTranslation[1] > self.MIN_YCOORDS_TRANS :
			self.moveMotor("front", "F1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , False)
			self.moveMotor("front", "F2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , False)
			self.moveMotor("back", "B1", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM , False)
			self.moveMotor("back", "B2", (abs(coordsTranslation[1])/self.MAX_YCOORDS_TRANS) * self.MAXIMUM_PWM, False)
			
		
		# Translation droite 
		elif coordsTranslation[0] > self.MAX_XCOORDS_TRANS  and coordsTranslation[0] < self.MAX_XCOORDS_DEAD and coordsTranslation[1] > self.MIN_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_DEAD :
			self.moveMotor("front", "F1", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, True)
			self.moveMotor("front", "F2", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, False)
			self.moveMotor("back", "B1", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, True)
			self.moveMotor("back", "B2", (abs(coordsTranslation[0])/self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, False)
		
		# Translation gauche 
		elif coordsTranslation[0] > self.MIN_XCOORDS_TRANS  and coordsTranslation[0] < self.MIN_XCOORDS_DEAD and coordsTranslation[1] > self.MIN_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_DEAD :
			self.moveMotor("front", "F1", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM , False)
			self.moveMotor("front", "F2", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM , True)
			self.moveMotor("back", "B1", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, False)
			self.moveMotor("back", "B2", (abs(coordsTranslation[0])/ self.MAX_XCOORDS_TRANS) * self.MAXIMUM_PWM, True)
			
		
		# Diagonale haut gauche 
		elif coordsTranslation[0] > self.MIN_XCOORDS_TRANS and coordsTranslation[0] < self.MIN_XCOORDS_DEAD  and coordsTranslation[1] > self.MAX_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_TRANS :
			self.moveMotor("front", "F1", 0 , False)
			self.moveMotor("front", "F2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, True)
			self.moveMotor("back", "B1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, True)
			self.moveMotor("back", "B2", 0, False)
			
		# Diagonale haut droite 
		elif coordsTranslation[0] > self.MAX_XCOORDS_DEAD  and coordsTranslation[0] < self.MAX_XCOORDS_TRANS and coordsTranslation[1] > self.MAX_YCOORDS_DEAD and coordsTranslation[1] < self.MAX_YCOORDS_TRANS :
			self.moveMotor("front", "F1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, True)
			self.moveMotor("front", "F2", 0, False)
			self.moveMotor("back", "B1", 0, True)
			self.moveMotor("back", "B2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, True)	
		
		# Diagonale bas gauche 
		elif coordsTranslation[0] > self.MIN_XCOORDS_TRANS and coordsTranslation[0] < self.MIN_XCOORDS_DEAD  and coordsTranslation[1] > self.MAX_YCOORDS_TRANS and coordsTranslation[1] < self.MIN_YCOORDS_DEAD :
			self.moveMotor("front", "F1", 0 , False)
			self.moveMotor("front", "F2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, False)
			self.moveMotor("back", "B1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, False)
			self.moveMotor("back", "B2", 0, True)
			
		# Diagonale bas droite 
		elif coordsTranslation[0] > self.MAX_XCOORDS_DEAD  and coordsTranslation[0] < self.MAX_XCOORDS_TRANS and coordsTranslation[1] > self.MAX_YCOORDS_TRANS and coordsTranslation[1] < self.MIN_YCOORDS_DEAD : 
			self.moveMotor("front", "F1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, False)
			self.moveMotor("front", "F2", 0, False)
			self.moveMotor("back", "B1", 0, True)
			self.moveMotor("back", "B2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (self.MAX_XCOORDS_TRANS + self.MAX_YCOORDS_TRANS)) * self.MAXIMUM_PWM, False)	
		
		
