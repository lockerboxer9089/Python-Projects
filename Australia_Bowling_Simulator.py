from getpass import getpass
import random

class bowler:
    def __init__(self, bowlername, bowlerspeed, bowlerball):
        self.bowlername = bowlername
        self.bowlerspeed = bowlerspeed
        self.bowlerball = bowlerball

    def bowlaball(self):
        print("Bowler = ", self.bowlername, "Speed = ", self.bowlerspeed, "Ball length = ", self.bowlerball)

def mainfunc():
    x = random.randrange  
    if x in range(0,30):
        PatCummins = bowler("Pat Cummins", y, "Short ball")
        PatCummins.bowlaball
    elif x in range(30,80):
        PatCummins = bowler("Pat Cummins", y, "Good length ball")
        PatCummins.bowlaball()
    elif x in range(80,100):
        PatCummins = bowler("Pat Cummins", y, "Overpitched ball")
        PatCummins.bowlaball()
user_input = getpass("Enter bowler name: ").lower()
if user_input == "cummins":
    mainfunc()

