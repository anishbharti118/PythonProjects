#importing Libraries
import math
import random

#Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

#Generating random number between lower and upper bounds
x = random.randint(lower, upper)

#Maximum number og guessses
t = round(math.log(upper-lower+1, 2))
print("\n\tYou have only", t,"chances to guess the Number\n")

#Number of guesses counter
c=0

#Algorithm
while c < t:
    c+=1

    #taking user's guess as input
    guess = int(input("Guess a number: "))

    #condition testing
    if x==guess:
        print("Congratulations! you guessed right in", c,"chances")
        break
    elif x>guess:
        print("You guessed less")
    else:
        print("You guessed more")

#Losing condition check
if c>t:
    print("The number is: ", x)
    print("Better Luck Next Time!")