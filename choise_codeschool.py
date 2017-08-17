import random
computer_choice = ["rock", "paper", "python"]

user_choice = input("enter the choise - rock, paper or python :")

a = random.choice(computer_choice)

if user_choice == a :
    print("draw, the same chosed pc: ", a)
else: print("you are lose, pc choise is: ", a)