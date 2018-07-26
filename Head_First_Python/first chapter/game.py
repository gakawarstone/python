import random

number = random.randint(1, 20)
win = 0

for i in range(5):
    your_number = int(input("please enter number from 0 to 20: "))
    if your_number == number:
        print("you win")
        win = 1
        break
    elif your_number > number:
        print("try less")
    elif your_number < number:
        print("try more")

if win == 0:
    print("you lose")
