'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.

3.  Create a program that simulates a magic 8-ball​
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good
'''

#dice roll
'''
import random
random_number = random.randint(1,6) 
print(f"You have rolled a {random_number}")
'''

#experiment
'''
import random
print(random.randrange(0,3))  #returns value of index?
'''

#8-ball 

#responses
responses = ['Outlook is good',
             'Ask again later',
             'Yes',
             'No',
             'Most likey no',
             'Most likely yes',
             'Maybe',
             'Outlook is not good']

#question
question = input("Ask a question and the magical 8-ball will decide your fate. ")

#response
import random
random_index = random.randint(0,7)
print(f"The magical 8-ball says: {responses[random_index]}")