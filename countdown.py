import time
t = int(input("enter the countdown timer in seconds"))
def countdown(n):
    while n:
        mins,sec = divmod(n,60)
        timeformat = f"{mins:02d}:{sec:02d}"
        print(timeformat,end = '\r')
        time.sleep(1)
        n-=1
    print("stop")
countdown(t)