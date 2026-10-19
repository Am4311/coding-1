# conditional if/else logic - these are keywords that instruct your program to do speific instructions based on specific data or conditions

# condititional syntax (how it is written)

#def billMachine():
# condititional syntax (how it is written)
   # bill_amount = int(input("Please type in a bill tender (1,5,10): "))
# if usually indicates that something is a possible option
    #if bill_amount == 1:
        #print("here are 4 quarters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
    #elif bill_amount == 5:
        #print("here are 20 quarters")
    #elif bill_amount == 10:
        #print("here are 50 quarters")
    #elif bill_amount == 20:
        #print("sorry cant accepts 20s. here's your money back")
    #elif bill_amount == 50:
        #print("sorry cant accepts 50s. here's your money back")
# else is ALWAYS your last option. 
    #else: 
        #print("sorry amount entered is not correct. your burnt")


#def college():
    #grade=  int(input("please type in your grade: "))
    #if grade > 90:
        #templeUApp()
    #else:
        #ccpApp()

#def ccpApp():
    #print("congrats please complete the community college app with the following code")
    #print("238293")

#def templeUApp():
    #print("congrats please complete the templa u app with the following code")
    #print("a7ds78sd") 

#college()

# using calculator functions from the calculator.py file to perform calculations


from prompt_toolkit import choice


#def calculate_add():
#    print("Program has started: please type in 2 numbers to add ")
#    num1 = int(input())
#    num2 = int(input())
 #   print( num1 + num2)
  #  print("Program has ended. ")

#def calculate_subtract():
 #   print("Program has started: please type in 2 numbers to subtract ")
  #  num1 = int(input())
   # num2 = int(input())
    #print( num1 - num2)
    #print("Program has ended. ")


#def calculate_multiply():
 #   print("Program has started: please type in 2 numbers to multiply ")
  #  num1 = int(input())
   # num2 = int(input())
    #print( num1 * num2)
    #print("Program has ended. ")

#def calculate_divide():
 #   print("Program has started: please type in 2 numbers to divide ")
  #  num1 = int(input())
   # num2 = int(input())
    #print( num1 / num2)
    #print("Program has ended. ")

#choice = int(input("Please type in a number to select a calculation: 1 for add, 2 for subtract, 3 for multiply, 4 for divide: "))

#if choice == 1:
#    calculate_add()
#elif choice == 2:
 #   calculate_subtract()
#elif choice == 3:  
 #   calculate_multiply()
#elif choice == 4:
    #calculate_divide()  



#def ticketprogram():
 #   print("Program has started: please type in your age to see to see the price of your ticket  ")
   # age = input()
    #if age < 6:
  #      print("your ticket is $8.00")
  #  elif age >= 8 and age <= 20:
   #     print("ticket price = $12.00")
 #   elif age >= 21 and age <= 60:
  #      print("ticket price = $20.00")
   # elif age >= 61:
    #   print("ticket price = free")