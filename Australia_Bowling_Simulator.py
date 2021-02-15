import random
class bowler:
    def __init__(self, name, ballspeed, balllength):
        self.name = name
        self.ballspeed = ballspeed
        self.balllength = balllength
    def mainfunc(self):
        print("The bowler is :", self.name, "The ball speed is :", self.ballspeed, "The length of the ball is :", self.balllength)

def cumminsover():
    for i in range(0,8):
        x = random.randrange(0,100)
        y = random.randrange(138,147)
        if x in range(0,30):
            PatCummins = bowler("Pat Cummins", y, "Short ball")
            PatCummins.mainfunc
        elif x in range(30,80):
            PatCummins = bowler("Pat Cummins", y, "Good length ball")
            PatCummins.mainfunc()
        elif x in range(80,100):
            PatCummins = bowler("Pat Cummins", y, "overpitched ball")
            PatCummins.mainfunc()
        else:
            print("ERROR")  

cumminsover()
