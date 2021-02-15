import random
class Bowler:
	def __init__(self, name, speed, length):
		self.name = name
		self.speed = speed
		self.length = length
	def mainfunc(self):
		print("Bowler is :", self.name, "speed = ", self.speed, "length is :", self.length)
for i in range(0,6):
	a = random.randrange(145, 150)
	x = random.randrange(0,100)
	if x in range(0,30):
		P1 = Bowler("Cummmins", a, "good")
		P1.mainfunc()
