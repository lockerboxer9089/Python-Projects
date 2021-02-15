import random
NumShortBall = 0
NumGoodLengthBall = 0
NumOverpitchedBall = 0
class Bowler:
	def __init__(self, name, ballbowled, speed):
		self.name = name
		self.ballbowled = ballbowled
		self.speed = speed
	def bowlaball(self):
		print("The bowler is :", self.name, "The ball bowled is a :", self.ballbowled, "The speed of the ball is :", self.speed)
bowler = str(input("Enter name of bowler. Options are : Cummins, Hazlewood, Starc and Lyon. :"))
bowler = bowler.lower()
if bowler == 'cummins':
	for i in range(0,6):
		x = random.randrange(0,6)
		if x in range(0,30):
			PatCummins = Bowler("Pat Cummins" + "Ball bowled is a short ball", random.randrange(138, 147))
			PatCummins.bowlaball()
		elif x in range(30,80):
			PatCummins = Bowler("Pat Cummins" + "Ball bowled is a good length ball", random.randrange(138,147))
			PatCummins.bowlaball()
		elif x in range(80, 100):
			PatCummins = Bowler("Pat Cummins" + "Ball bowled is a overpitched ball", random.randrange(138,147))
			PatCummins.bowlaball()
for i in range(0,1000):
	x = random.randrange(0,100)
	if x in range(0,29+1):
		print("Ball bowled is a short ball")
		NumShortBall = NumShortBall + 1
	elif x in range(30,79+1):
		print("Ball bowled is a good length ball")
		NumGoodLengthBall = NumGoodLengthBall + 1
	elif x in range(80,99+1):
		print("Ball bowled is a overpitched ball")
		NumOverpitchedBall = NumOverpitchedBall + 1
	else:
		print("Error! Number not counted is ", x)		
print("Number of short balls is :", NumShortBall)
print("Number of goodlength balls bowled = :", NumGoodLengthBall)
print("Number of overpitched balls bowled = :", NumOverpitchedBall)
