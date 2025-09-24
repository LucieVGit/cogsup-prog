"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
from random import randint

def right_answer(n):
    """ Check if string 'answer' was answered correctly."""
    print(f"My guess is : {n}")
    clue = input("Is it this number ? ") # Ask the user for their clue
    if clue == "Too high":
        return randint(1,n-1)  # new n that is lower
    elif clue == "Too low":
        return randint(n+1,100) # new n that is higher
    elif clue == "Yes":
        print("I have guessed your number !!! Have a nice day :)")
        return None # signal the loop to stop
    else:
        print("Please, enter a correct answer : Too low, Too high or Yes")  
    return n # keep the same guess if input was invalid

print("Think of a number between 1 and 100")
print("This program will have to find it! For each guess made by the computer answer by : Too high or Too low, to give clues about your number.")
print("If the program has guessed your number, answer by : Yes")

n = randint(1,100) # First guess 

while n is not None:
    n = right_answer(n) # calls the function and update 'n' with the new guess
