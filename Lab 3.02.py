'''
############
Lab 3.02
############
Lab Exercise 1
--------------
Create a function, birthday_song, that prints out the happy birthday song to whatever name is input as an argument. The contract should be:

  # Name: birthday_song
  # Purpose: birthday_song prints out a personalized birthday song
  # Arguments: name, string
  # Returns: none
  def birthday_song(name):
     #your code goes here

#happy birthday
def birthday_song(name):
  print("Happy birthday to you! \n"
  "Happy birthday to you! \n"
  f"Happy birthday dear {name}! \n"
  "Happy Birthday to you!")

#experiment
birthday_song("Bob")

Lab Exercise 2
---------------
Create a function that randomly picks 5 cards from a deck 

The cards can repeat

Write out the contract for this function using the list.

number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#contract
  #name- pick_5_cards
  #purpose- pick_5_cards prints out 5 randomized cards
  #arguments- none
  #returns- none 
  
Bonus
Practice passing in lists as an argument to a function.

What is different about passing in a list as an argument?

Read about list aliasing in section 3.4 of the associated reading, and write down what is happening in this case.
Remember, the associated reading is in the "SWBAT" section on moodle!
'''
#pick 5 cards
def pick_5_cards():
  number = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  #assigns card index to 5 cards
  import random
  random1 = (random.randint(0,12))
  random2 = (random.randint(0,12))
  random3 = (random.randint(0,12))
  random4 = (random.randint(0,12))
  random5 = (random.randint(0,12))
  
  #prints cards
  print("Your cards are: \n"
  f"{number[random1]}\n"
  f"{number[random2]}\n"
  f"{number[random3]}\n"
  f"{number[random4]}\n"
  f"{number[random5]}")

#call function
pick_5_cards()


