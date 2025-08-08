import time
def addition(n1,n2):
    n = n1+n2
    return n
def sub(n1,n2):
    n = n1-n2
    return n
def multiply(n1,n2):
    n = n1*n2
    return n
def div(n1,n2):
    try:
        n = n1/n2
        return n
    except ZeroDivisionError:
        time.sleep(0.5)
        return print("the number cannot be divided by zero")
def modulo(n1,n2):
    n = n1%n2
    return n
def power(n1,n2):
    n= n1**n2
    return n
while True:
    print("Welcome to the calculator\n 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division\n 5 - Modulo\n 6 - Power")
    time.sleep(1)
    print("which operation do you want to perform")
    time.sleep(0.5)
    choice = int(input("enter the choice in numbers: "))
    time.sleep(0.5)
    if choice>6 or choice<1:
        print("invalid choice")
    try:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        time.sleep(0.4)
    except ValueError:
        time.sleep(0.5)
        print("please enter only numbers")
        continue
    if choice == 1:
        print(num1,'+',num2,'=',addition(num1,num2))
    elif choice == 2:
        print(num1,'-',num2,'=',sub(num1,num2))
    elif choice == 3:
        print(num1,'x',num2,'=',multiply(num1,num2))
    elif choice == 4:
        print(num1,'/',num2,'=',div(num1,num2))
    elif choice == 5:
        print(num1,'%',num2,'=',modulo(num1,num2))
    elif choice == 6:
        print(num1,'^^',num2,'=',power(num1,num2))
    time.sleep(1)
    next = input("Do you want to perform next calculation?(yes/no)")
    if next == 'no':
        break

