#user's name
name = input("Enter your name. ")

#instructions
print("This is the Oregon Trail. \n"
"Your goal is to travel from Independence, Missouri to Oregon City, Oregon (2000 miles) by Dec 31st. \n"
"However, the trail is arduous. \n"
"You can hunt and rest, but you have to get there before winter! \n"
"You will have 500 lbs of food and 5 health. \n"
"Each day, you will eat 5 lbs of food \n"
"Your options on this journey are: \n"
"travel: moves you randomly between 30-60 miles and takes 3-7 days (random). \n"
"rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random). \n"
"hunt: adds 100lbs of food and takes 2-5 days (random). \n"
"status: lists food, health, distance traveled, and day. \n"
"help: lists all the commands. \n"
"quit: will end the game. \n"
"Will you be able to survive and make it to Oregon city or will you die before and when winter comes?")

#statuses
food = 500
health = 5
months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
miles = 2000




#options
def travel():
    import random

def rest():
    import random

def hunt():
    import random

def status():
    pass

def help():
    print("Your options are: \n"
    "travel: moves you randomly between 30-60 miles and takes 3-7 days (random). \n"
    "rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random). \n"
    "hunt: adds 100lbs of food and takes 2-5 days (random). \n"
    "status: lists food, health, distance traveled, and day. \n"
    "help: lists all the commands. \n"
    "quit: will end the game.")

def quit():
    print("I see you gave up. \n"
    "What a shame. \n"
    "You have died and vultures are now feeding on your dead remains.")

