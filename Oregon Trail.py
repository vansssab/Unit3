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
current_day = 1
current_month = 3


#options
def travel():
    import random
    global current_day
    global current_month
    global miles
    days_passed = random.randint(3, 7)
    current_day += days_passed
    if current_day > 31 and months_with_31_days:
        current_month += 1
        current_day = 1
    elif current_day > 30:
        current_month += 1
        current_day = 1
    miles -= random.randint(30, 60)
    print(f"{days_passed} have passed. \n"
    f"You have traveled {miles} miles. \n"
    f"The date is now {current_month}/{current_day}.")

def rest(): 
    import random
    global current_day
    global current_month
    global health
    days_passed2= random.randint(2, 5)
    current_day += days_passed2
    if current_day > 31 and months_with_31_days:
        current_month += 1
        current_day = 1
    elif current_day > 30:
        current_month += 1
        current_day = 1
    health += 1
    if health > 5:
        print("Your health can not exceed 5 levels.")
        health = 5
    else:
        print("Your health has increased. \n"
        f"Your health is now {health}")
    print(f"{days_passed2} have passed. \n"
    f"The date is now {current_month}/{current_day}.")

def hunt():
    import random
    global food
    global current_day
    global current_month
    food += 100
    days_passed3= random.randint(2, 5)
    current_day += days_passed3
    if current_day > 31 and months_with_31_days:
        current_month += 1
        current_day = 1
    elif current_day > 30:
        current_month += 1
        current_day = 1
    print("You have gained 100 lbs of food. \n"
    f"You now have {food} lbs of food. \n"
    f"{days_passed3} have passed. \n"
    f"The date is now {current_month}/{current_day}.")
    
def status():
    print("Your stats are: \n"
    f"health = {health} health \n"
    f"food = {food} lbs \n"
    f"miles left = {miles} miles \n"
    f"current date = {current_month}/{current_day}")

def help():
    print("Your options are: \n"
    "travel: moves you randomly between 30-60 miles and takes 3-7 days (random). \n"
    "rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random). \n"
    "hunt: adds 100lbs of food and takes 2-5 days (random). \n"
    "status: lists food, health, distance traveled, and day. \n"
    "help: lists all the commands. \n"
    "quit: will end the game.")

def quit():
    print("You want to give up? \n"
    "What a shame. \n"
    "You have died and vultures are now feeding on your dead remains.")

#main program
while not current_month == 12 and not current_day == 31:
    pass

