from getpass import getpass
import random

class bowler:
    def __init__(bowlerobject, name, ballspeed, balllength):
        bowlerobject.name = name
        bowlerobject.ballspeed = ballspeed
        bowlerobject.balllength = balllength

    def bowlaball(abc):
        print("Bowler = ", abc.name, ":ball speed = ", abc.ballspeed, ":Length of the ball = ", abc.balllength)

def bowlanovercummins():
    for i in range(0,6):
        x = random.randrange(0,100)
        y = random.randrange(133,147)
        if x in range(0,30):
            PatCummins = bowler("Pat Cummins", y, "Short ball")
            PatCummins.bowlaball()
        elif x in range(30,80):
            PatCummins = bowler("Pat Cummins", y, "Good length ball")
            PatCummins.bowlaball()
        elif x in range(80,100):
            PatCummins = bowler("Pat Cummins", y, "overpitched ball")
            PatCummins.bowlaball()

def bowlanoverhazlewood():
    for i in range(0,6):
        x = random.randrange(0,100)
        y = random.randrange(131,143)
        if x in range(0,40):
            JoshHazlewood = bowler("Josh Hazlewood", y, "Short ball")
            JoshHazlewood.bowlaball()
