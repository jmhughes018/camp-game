# This program is designed so that four teams at a camp can enter
# secret phrases into a terminal in order to earn points
# and/or take away points from another team

import os
from myDict import myPhrases
import time

class Team(object):
    def __init__(self, color, points):
        self.color = color
        self.points = points
    def add_points(self, points):
        self.points += points
    def subtract_points(self, points):
        self.points -= points
       

def ask_for_phrase():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Well hello there!"    
    print "\nIf you want to see how the teams are doing, type the word 'points.'"
    userPhrase = raw_input("Or, if you have a password, type it in! ")
    return userPhrase

def evaluate_phrase(phrase):
    isValid = False
    phrase = phrase.strip().upper()
    if phrase in myPhrases:
        isValid = True
        myPhrases.remove(phrase)

    return isValid

def ask_for_team_name():
    print " "
    while True:
        userTeam = raw_input("(red, green, blue, or yellow) ")
        
        if userTeam.upper() == "YELLOW":
            return yellow
            break
        elif userTeam.upper() == "BLUE":
            return blue
            break
        elif userTeam.upper() == "GREEN":
            return green
            break
        elif userTeam.upper() == "RED":
            return red 
            break
        else:
            print "I'm sorry, I don't recognize that name..."

def display_points():
    print "\n"
    print "The red team has:        " + str(red.points) + " points."
    print "The blue team has:       " + str(blue.points) + " points."
    print "The green team has:      " + str(green.points) + " points."
    print "The yellow team has:     " + str(yellow.points) + " points."

def display_options():
    print "\nAlright, well you can either 'get points' or you can 'take points' from another team."
    while True:
        userAction = raw_input("Which would you like to do? ")
        userAction = userAction.upper()
        if userAction == "GET POINTS" or userAction == "TAKE POINTS":
            return userAction
            break
        else:
            print "\nSorry, I didn't get that. Please type either get points or take points"

def save_scores():
    f = open("scores.txt", "w")
    f.write(str(yellow.points) + "\n")
    f.write(str(blue.points) + "\n")
    f.write(str(red.points) + "\n")
    f.write(str(green.points) + "\n")
    f.close()

def initialize_scores():
    f = open("scores.txt", "w")
    f.write(str(0) + "\n")
    f.write(str(0) + "\n")
    f.write(str(0) + "\n")
    f.write(str(0) + "\n")
    f.close()


# control flow below



f = open("scores.txt", "r")
yellow_score = f.readline()
blue_score = f.readline()
red_score = f.readline()
green_score = f.readline()
f.close()

yellow = Team("yellow", int(float(yellow_score)))
blue = Team("blue", int(float(blue_score)))
red = Team("red", int(float(red_score)))
green = Team("green", int(float(green_score)))

while True:
    userPhrase = ask_for_phrase()
    if evaluate_phrase(userPhrase):
        print "\nThat's a match!"
        display_points()
        print "\n \nWhich team are you?" 
        userTeam = ask_for_team_name()
        action = display_options()
        if action == "TAKE POINTS":
            print "Which team would you like to take points from?"
            otherTeam = ask_for_team_name()
            otherTeam.subtract_points(25)
            userTeam.add_points(25)
        else:
            userTeam.add_points(50)
        display_points()
        save_scores()
        time.sleep(5)
    elif userPhrase.upper() == "POINTS":
        os.system('cls' if os.name == 'nt' else 'clear')
        display_points()
        time.sleep(5)
    elif userPhrase.upper() == "INITIALIZE POINTS":
        initialize_scores()
    elif userPhrase.upper() == "EXIT": #loop and a half
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print "Sorry, that's not a match!"
        time.sleep(1.5)
