import random
import time
print("Winning rule for the game ROCK PAPER SCISSORS are:\nRock vs Paper -> Paper wins\nRock vs Scissors -> Rock wins\nPaper vs Scissors -> Scissors wins")
time.sleep(1)
while True:
    print("Enter your Choice\n 1-Rock \n 2- Paper \n 3-Scissors\n")
    time.sleep(0.5)
    choice = int(input("Enter your choice:"))
    while choice>3 or choice<1:
        choice = int(input("Please enter the valid choice"))
    if choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Paper'
    else:
        user_choice = 'Scissors'
    print("User choice : ",user_choice)
    time.sleep(1)
    print("Now its a computer Turn.........")
    time.sleep(1)
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        computer_choice = 'Rock'
    elif comp_choice == 2:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'
    print("Computer choice is: ",computer_choice)
    time.sleep(1)
    print(user_choice, "vs" ,computer_choice)
    time.sleep(1)
    if choice == comp_choice:
        result = "draw"
    elif (choice ==1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = "Paper"
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = "Scissors"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "Rock"
    if result == "draw":
        print("<==== It's a Tie! ====>")
    elif result == user_choice:
        print("<===== User Wins =====>")
    else:
        print("<===== Computer Wins =====>")
    time.sleep(1)
    print("Do you Want to Play again ? (Y/N)")
    ans = input().lower()
    if ans == "n":
        break
print("Thanks For Playing!!!!")
