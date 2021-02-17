from getpass import getpass
import random
# Importing required libraries
class bowler: # Creating a bowler class
    def __init__(bowlerobject, name, ballspeed, balllength):
        bowlerobject.name = name
        bowlerobject.ballspeed = ballspeed
        bowlerobject.balllength = balllength

    def bowlaball(abc):
        print("Bowler = ", abc.name, ":ball speed = ", abc.ballspeed, ":Length of the ball = ", abc.balllength)

def bowlanovercummins(): #Creating a function to bowl 1 over from Cummins
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

def bowlanoverhazlewood(): #Creating a function to bowl 1 over from hazlewood
    for i in range(0,6):
        x = random.randrange(0,100)
        y = random.randrange(131,143)
        if x in range(0,40):
            JoshHazlewood = bowler("Josh Hazlewood", y, "Short ball")
            JoshHazlewood.bowlaball()
        elif x in range(40,90):
            JoshHazlewood = bowler("Josh Hazlewood", y, "Good length ball")
            JoshHazlewood.bowlaball()
        elif x in range(90,100):
            JoshHazlewood = bowler("Josh Hazlewood", y, "Overpitched")
            JoshHazlewood.bowlaball()

def bowlanoverstarc(): #Creating a function to bowl 1 over from starc
    for i in range(0,6):
        x = random.randrange(0,100)
        y = random.randrange(141,150)
        if x in range(0,30):
            MitchellStarc = bowler("Mitchell Starc", y, "Short ball:")
            MitchellStarc.bowlaball()
        elif x in range(30,70):
            MitchellStarc = bowler("Mitchell Starc", y, "Good length ball")
            MitchellStarc.bowlaball()
        elif x in range(70,100):
            MitchellStarc = bowler("Mitchell Starc", y, "Overpitched ball")
            MitchellStarc.bowlaball()
    
print(""" 
INFORMATION:
This program will simulate 1 over from any bowler of your choice. 
It will tell the bowler's name, speed of the ball bowled and the langth bowled.
You can choose any of the names that the program gives as options.
""") #Giving some information about the program
while True: #Main part of the program
    user_input = getpass("Enter bowler name: Options = Cummins, Hazlewood and Starc : Enter 'done' to stop the simulator: ").lower()
    if user_input == "cummins":
        bowlanovercummins()
    elif user_input == "hazlewood":
        bowlanoverhazlewood()
    elif user_input == "starc":
        bowlanoverstarc()
    elif user_input == "done":
        break
    else:
        print("""
ERROR:
Wrong name entered.
Pls enter one of the names that are in the options given by the program!
""")
#End of program
