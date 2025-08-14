import time
import random
print("Guess the number from 1 to 10")
time.sleep(0.7)
choice = random.randint(1,10)
while True:
    n = int(input("Enter the user choice:"))
    time.sleep(0.5)
    print("Now its a computer turn......")
    if n == choice:
        time.sleep(0.5)
        print("your Guess is corect!!!!")
        choice = random.randint(1,10)
    else:
        time.sleep(0.5)
        print("Your guess is wrong.....\n Please try again")
    s = input("Do you want to continue? (yes/no)")
    if s == 'no':
        break