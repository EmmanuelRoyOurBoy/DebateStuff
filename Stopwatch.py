import time
SecondCounter = int(input("How many seconds do you want to count down from? ")
for i in range(SecondCounter):
    print(str(SecondCounter-i) + " seconds remain")
    time.sleep(1)
