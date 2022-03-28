#user's name
from xxlimited import foo


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
minus_health_days = 2

#options
def travel():
    import random
    global current_day
    global current_month
    global miles
    global food
    global food_eaten_each_day
    days_passed = random.randint(3, 7)
    current_day += days_passed
    if current_day > 31 and months_with_31_days:
        current_month += 1
        days_passed -= 1
        current_day = days_passed
    elif current_day > 30:
        current_month += 1
        days_passed -= 1
        current_day = days_passed
    food_eaten_each_day *= days_passed
    food -= food_eaten_each_day
    miles_traveled = random.randint(30, 60)
    miles -= miles_traveled
    print(f"{days_passed} days have passed. \n"
    f"You have consumed {food_eaten_each_day} lbs of food \n"
    f"You have traveled {miles_traveled} miles. \n"
    f"The date is now {current_month}/{current_day}.")

def rest(): 
    import random
    global current_day
    global current_month
    global health
    global food
    global food_eaten_each_day
    days_passed2= random.randint(2, 5)
    current_day += days_passed2
    if current_day == 31 and months_with_31_days:
        current_month += 1
        days_passed2 -= 1
        current_day = days_passed2
    elif current_day > 30:
        current_month += 1
        days_passed2 -= 1
        current_day = days_passed2
    health += 1
    if health > 5:
        print("Your health can not exceed 5 levels.")
        health = 5
    else:
        print("Your health has increased by 1.")
    food_eaten_each_day *= days_passed2
    food -= food_eaten_each_day
    print(f"{days_passed2} days have passed. \n"
    f"You have consumed {food_eaten_each_day} lbs of food \n"
    f"The date is now {current_month}/{current_day}.")

def hunt():
    import random
    global food
    global current_day
    global current_month
    global food
    global food_eaten_each_day
    food += 100
    days_passed3= random.randint(2, 5)
    current_day += days_passed3
    if current_day > 31 and months_with_31_days:
        current_month += 1
        days_passed3 -= 1
        current_day = days_passed3
    elif current_day > 30:
        current_month += 1
        days_passed3 -= 1
        current_day = days_passed3
    food_eaten_each_day *= days_passed3
    food -= food_eaten_each_day
    print(f"{days_passed3} days have passed. \n"
    "You have gained 100 lbs of food. \n"
     f"You have consumed {food_eaten_each_day} lbs of food \n"
    f"The date is now {current_month}/{current_day}.")
    
def status():
    print("Your stats are: \n"
    f"health = {health} health \n"
    f"food = {food} lbs left\n"
    f"miles left = {miles} miles left\n"
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
    import random
    food_eaten_each_day = 5
    print(f"Today's date is {current_month}/{current_day}.")
    choice = input("What would you like to do (travel, rest, hunt, status, help, quit)? ")
    if choice == 'travel':
        travel()
    elif choice == 'rest':
        rest()
    elif choice == 'hunt':
        hunt()
    elif choice == 'status':
        status()
    elif choice == 'help':
        help()
    elif choice == 'quit':
        quit()
    else:
        print("That is not an option. Try again.")
    
    #health decreases twice a month
    if current_month + 1:
        minus_health_days = 2
        if minus_health_days > 0:
            random_health_day = random.randint(1, 30)
            if current_day == random_health_day:
                health_decrease = random.randint(1, 3)
                health -= health_decrease
                minus_health_days -= 1
                print(f"Your health has decreased by {health_decrease} because of the hardships of the travel.")
    
    #deaths
    if health <= 0:
        print(f"Your health is {health}.")
        print("You have died due to a heart attack.")
        print("You lose. Game Over.")
        break

    if food <= 0:
        print(f"Your food storage is {food} lbs. \n"
        "YOu have died due to starvation. \n"
        "You lose. Game Over.")
        break

#game end
if current_month == 12 and current_day == 31:
    if miles <= 0:
        print("You made it to Oregon City! \n"
        "You win!")
    elif miles > 0:
        print("You have not made it to Oregon City in time. \n"
        "Therefore, you got frostbite and died to hypothermia. \n"
        "Game Over. You lose.")




