import random

class Bowler:
	def __init__(self, name, ProbShort, ProbGood, ProbOverP, ProbWicket):
		self.name = name
		self.ProbShort = ProbShort
		self.ProbGood = ProbGood
		self.ProbOverP = ProbOverP
		self.ProbWicket = ProbWicket
	
	def BowlABall(self):
		CumulShort = self.ProbShort
		CumulGood = CumulShort + self.ProbGood
		CumulOverP = CumulGood + self.ProbOverP

		length = random.uniform(0,1)
		if length < CumulShort:
			print("Ball bowled is a short ball")
		elif length < CumulGood:
			print("Ball bowled is a good length ball")
		elif length < CumulOverP:
			print("Ball bowled is an overpitched ball")
		else:
			print("Error!")

		wicket = random.uniform(0,1)
		BALLS = 0
		if wicket > self.ProbWicket:
			print("No wicket this ball")
			BALLS = BALLS + 1
		elif wicket <= self.ProbWicket:
			print("Wicket!, Number of balls before previous wicket = ", BALLS)
			BALLS = 0


PatCummins = Bowler("Pat Cummins", 0.3, 0.5, 0.2, 0.05)
JoshHazlewood = Bowler("Josh Hazlewood", 0.4, 0.5, 0.1, 0.03)
MitchellStarc = Bowler("Mitchell Starc", 0.25, 0.4, 0.35, 0.04)
NathanLyon = Bowler("Nathan Lyon", 0.2, 0.6, 0.2, 0.06)
while True:
	user_input = str(input("Enter bowler name, Enter 'done' to end the simulator, Option = Cummins, Hazlewood, Starc and Lyon -")).lower()
	if user_input == 'cummins':
		for i in range(0,6):
			PatCummins.BowlABall()
	elif user_input == 'hazlewood':
		for i in range(0,6):
			JoshHazlewood.BowlABall()
	elif user_input == 'starc':
		for i in range(0,6):
			MitchellStarc.BowlABall()
	elif user_input == 'lyon':
		for i in range(0,6):
			NathanLyon.BowlABall()
	elif user_input == 'done':
		break
