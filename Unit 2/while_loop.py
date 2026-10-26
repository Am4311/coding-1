# loop - A loop is a construct that repeats itself. in programming a loop allows to repeat code instructions.

#there is two types of loops: for loop and while loop

# While loop - a type of loop where so long as a condition is equal to ture it will keep running forever.

# The keyword is while.

# Syntax:
#num = 4
#while 2 + 2 == num:
    #print("Program is running...")
#num = int(input("please enter a new number: "))
#while loops will ALWAYS run unless you change thr condition. We can do this by writing instructions to manually change it. 




#def gussingGame():
    #correctAnswer = 10 
    #userGuess = int(input("Please type in a number to guess"))
    #attemps = 0

    #while userGuess != correctAnswer:
        #print("Wrong answer, please try again")
        #userGuess = int(input("Please type in a number to guess"))
        #attemps += 1
        #print('Number of attempts: ' + str(attemps))
        #userGuess = int(input("Please type in a number to guess"))



#def passwordReset():
    #password = "TwentyThousandEmusVsOneMoose"
    #userPassword = input("Please enter your current password: ")
    #attempts = 3
    
    #while userPassword != password and attempts > 0:
     #   print("Incorrect password, please try again.")
      #  attempts -= 1
       # print("Number of attempts: " + str(attempts))
        #if attempts == 0:
         #   print("You have been locked out.")
        #userPassword = input("Please enter your current password: ")
            
#def vendingMachine():
    #item = input("Please enter the item you would like to purchase: ")
    #item = nachoChips
    #nachochips = B3


    #BBQChips = G4
    #item = BBQChips
    
    #item = PlainChips
    #PlainChips = G7

    #item = Water
    #Water = D3

    #item = ColaSoda 

    #ColaSoda = D4


#import random

#radint = random.randint(1, 7)
#print(radint)
#r = roll 
#q = quit

import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    while user_choice != 'quit':
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
        else:
            print(f"Computer chose: {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):