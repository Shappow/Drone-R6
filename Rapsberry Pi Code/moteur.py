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
	
	MAXIMUM_PWM = 65500
	
	# Constantes Translation
	MAX_XCOORDS_TRANS = 512
	MIN_XCOORDS_TRANS = -512
	
	MAX_YCOORDS_TRANS= 512
	MIN_YCOORDS_TRANS = -512
	
	# Constantes Rotation
	MAX_XCOORDS_ROT= 512
	MAX_YCOORDS_ROT = 512
	
	MIN_XCOORDS_ROT = -512
	MIN_YCOORDS_ROT = -512
	
	# Constantes Dead Point
	
	MAX_XCOORDS_DEAD = 200
	MIN_XCOORDS_DEAD = -200
	
	MAX_YCOORDS_DEAD= 200
	MIN_YCOORDS_DEAD = -200
	
	def __init__ (self, EnA, EnB, backIn1,backIn2,backIn3,backIn4,frontEnA, frontEnB, frontIn1,frontIn2,frontIn3,frontIn4) :
		pinBackMotors  = {
			enA : EnA,
			enB : EnB,
			in1 : backIn1,
			in2 : backIn2,
			in3 : backIn3,
			in4 : backIn4
		} 
		pinfrontMotors  = {
			enA : EnA,
			enB : EnB,
			in1 : frontIn1,
			in2 : frontIn2,
			in3 : frontIn3,
			in4 : frontIn4
		} 
		GPIO.setmode(GPIO.BOARD)
		
		
		GPIO.setup(EnA,GPIO.OUT)
		GPIO.setup(EnB,GPIO.OUT)
		
		pwmEnA = GPIO.PWM(EnA,GPIO.OUT)
		pwmEnB = GPIO.PWM(EnB,GPIO.OUT)
		
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
	def moveMotor(self, side, motor, speed, direction) :
		if side == "front" : 
			if en == "F1" :
			
				if direction : 
					GPIO.output(pinFrontMotors["in1"], GPIO.LOW)
					GPIO.output(pinFrontMotors["in2"], GPIO.HIGH)
				else : 
					GPIO.output(pinFrontMotors["in2"], GPIO.LOW)
					GPIO.output(pinFrontMotors["in1"], GPIO.HIGH)
				pwmEnA.start(speed)
			elif en == "F2" :
				if direction : 
					GPIO.output(pinFrontMotors["in4"], GPIO.LOW)
					GPIO.output(pinFrontMotors["in3"], GPIO.HIGH)
				else : 
					GPIO.output(pinFrontMotors["in3"], GPIO.LOW)
					GPIO.output(pinFrontMotors["in4"], GPIO.HIGH)
				pwmEnB.start(speed)
			return
		elif side == "back" : 
			if en == "B2" :
				if direction : 
					GPIO.output(pinBackMotors["in1"], GPIO.LOW)
					GPIO.output(pinBackMotors["in2"], GPIO.HIGH)
				else : 
					GPIO.output(pinBackMotors["in2"], GPIO.LOW)
					GPIO.output(pinBackMotors["in1"], GPIO.HIGH)
					pwmEnA.start(speed)
			elif en == "B1" :
				if direction : 
					GPIO.output(pinBackMotors["in3"], GPIO.LOW)
					GPIO.output(pinBackMotors["in4"], GPIO.HIGH)
				else : 
					GPIO.output(pinBackMotors["in4"], GPIO.LOW)
					GPIO.output(pinBackMotors["in3"], GPIO.HIGH)
				pwmEnB.start(speed)
			return 
		else : 
			print ("error, no side found")
	
	# TODO : Définir pwm et range des coordonnées
	def rotation(self, coordsRotation) :
		coordsRotation[0] = min(max(coordsRotation[0], MIN_XCOORDS_ROT, MAX_XCOORDS_ROT))
                                
		if coordsRotation[0] < MAX_XCOORDS_DEAD and coordsRotation[0] > MIN_XCOORDS_DEAD :
			return
		# rotationClockWise 
		elif coordsRotation > 0 :
			moveMotor("front", "F1", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 0)
			moveMotor("front", "F2", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 0)
			moveMotor("back", "B3", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 1)
			moveMotor("back", "B4", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 1)
		elif coordsRotation < 0 :
			moveMotor("front", "F1", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 1)
			moveMotor("front", "F2", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 1)
			moveMotor("back", "B3", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 0)
			moveMotor("back", "B4", (abs(coordsRotation[0])/MAX_XCOORDS_ROT) * MAXIMUM_PWM , 0)
	
	# TODO : Définir pwm et range des coordonnées
	def translation(self, coordsTranslation) :
		coordsTranslation[0] = min(max(coordsTranslation[0], MIN_XCOORDS_TRANS, MAX_XCOORDS_TRANS))
		coordsTranslation[1] = min(max(coordsTranslation[1], MIN_YCOORDS_TRANS, MAX_YCOORDS_TRANS))
		# Dead Point
		if (coordsTranslation[0] < MAX_XCOORDS_DEAD)  and (coordsTranslation[0] > MIN_XCOORDS_DEAD) and (coordsTranslation[1] < MAX_YCOORDS_DEAD)  and (coordsTranslation[1] > MIN_YCOORDS_DEAD) :
			return
		
		# Avancée 
		elif (coordsTranslation[0] > MIN_XCOORDS_DEAD) and coordsTranslation[0] < MAX_XCOORDS_DEAD and coordsTranslation[1] > MAX_YCOORDS_DEAD and coordsTranslation[1] < MAX_YCOORDS_TRANS :
			moveMotor("front", "F1", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM , 0)
			moveMotor("front", "F2", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM , 1)
			moveMotor("back", "B1", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM , 1)
			moveMotor("back", "B2", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM, 0)
		
		# Recul 
		elif coordsTranslation[0] > MIN_XCOORDS_DEAD  and coordsTranslation[0] < MAX_XCOORDS_DEAD and coordsTranslation[1] > MIN_YCOORDS_DEAD and coordsTranslation[1] < MIN_YCOORDS_TRANS :
			moveMotor("front", "F1", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM , 1)
			moveMotor("front", "F2", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM , 0)
			moveMotor("back", "B1", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM , 0)
			moveMotor("back", "B2", (abs(coordsTranslation[1])/MAX_YCOORDS_TRANS) * MAXIMUM_PWM, 1)
			
		
		# Translation droite 
		elif coordsTranslation[0] > MAX_XCOORDS_TRANS  and coordsTranslation[0] < MAX_XCOORDS_DEAD and coordsTranslation[1] > MIN_YCOORDS_DEAD and coordsTranslation[1] < MAX_YCOORDS_DEAD :
			moveMotor("front", "F1", (abs(coordsTranslation[0])/MAX_XCOORDS_TRANS) * MAXIMUM_PWM, 0)
			moveMotor("front", "F2", (abs(coordsTranslation[0])/MAX_XCOORDS_TRANS) * MAXIMUM_PWM, 1)
			moveMotor("back", "B1", (abs(coordsTranslation[0])/MAX_XCOORDS_TRANS) * MAXIMUM_PWM, 1)
			moveMotor("back", "B2", (abs(coordsTranslation[0])/MAX_XCOORDS_TRANS) * MAXIMUM_PWM, 0)
		
		# Translation gauche 
		elif coordsTranslation[0] > MIN_XCOORDS_TRANS  and coordsTranslation[0] < MIN_XCOORDS_DEAD and coordsTranslation[1] > MIN_YCOORDS_DEAD and coordsTranslation[1] < MAX_YCOORDS_DEAD :
			moveMotor("front", "F1", (abs(coordsTranslation[0])/ MAX_XCOORDS_TRANS) * MAXIMUM_PWM , 1)
			moveMotor("front", "F2", (abs(coordsTranslation[0])/ MAX_XCOORDS_TRANS) * MAXIMUM_PWM , 0)
			moveMotor("back", "B1", (abs(coordsTranslation[0])/ MAX_XCOORDS_TRANS) * MAXIMUM_PWM, 0)
			moveMotor("back", "B2", (abs(coordsTranslation[0])/ MAX_XCOORDS_TRANS) * MAXIMUM_PWM, 1)
			
		
		# Diagonale haut gauche 
		elif coordsTranslation[0] > MIN_XCOORDS_TRANS and coordsTranslation[0] < MIN_XCOORDS_DEAD  and coordsTranslation[1] > MAX_YCOORDS_DEAD and coordsTranslation[1] < MAX_YCOORDS_TRANS :
			moveMotor("front", "F1", (0 , 0))
			moveMotor("front", "F2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 0)
			moveMotor("back", "B1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 1)
			moveMotor("back", "B2", (0, 0))
			
		# Diagonale haut droite 
		elif coordsTranslation[0] > MAX_XCOORDS_DEAD  and coordsTranslation[0] < MAX_XCOORDS_TRANS and coordsTranslation[1] > MAX_YCOORDS_DEAD and coordsTranslation[1] < MAX_YCOORDS_TRANS :
			moveMotor("front", "F1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 0)
			moveMotor("front", "F2", (0, 0))
			moveMotor("back", "B1", (0, 1))
			moveMotor("back", "B2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 0)	
		
		# Diagonale bas gauche 
		elif coordsTranslation[0] > MIN_XCOORDS_TRANS and coordsTranslation[0] < MIN_XCOORDS_DEAD  and coordsTranslation[1] > MAX_YCOORDS_TRANS and coordsTranslation[1] < MIN_YCOORDS_DEAD :
			moveMotor("front", "F1", (0 , 0))
			moveMotor("front", "F2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 1)
			moveMotor("back", "B1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 0)
			moveMotor("back", "B2", (0, 0))
			
		# Diagonale bas droite 
		elif cocoordsTranslation[0] > MAX_XCOORDS_DEAD  and coordsTranslation[0] < MAX_XCOORDS_TRANS and coordsTranslation[1] > MAX_YCOORDS_TRANS and coordsTranslation[1] < MIN_YCOORDS_DEAD : 
			moveMotor("front", "F1", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 1)
			moveMotor("front", "F2", (0, 0))
			moveMotor("back", "B1", (0, 1))
			moveMotor("back", "B2", ((abs(coordsTranslation[0])+ abs(coordsTranslation[1]))/ (MAX_XCOORDS_TRANS + MAX_YCOORDS_TRANS)) * MAXIMUM_PWM, 1)	
		
		
