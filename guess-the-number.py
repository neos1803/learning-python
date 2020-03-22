from random import randint

x = 3
trueNumber = randint(0, 10)
while (x >= 1):
    print("You have ", x, " chance")
    n = int(input("Guess the number: "))

    if n > trueNumber :
        print("You need to guess lower!")
    elif n < trueNumber :
        print("You need to guess higher!")
    else :
        print("You guess it right, ", trueNumber, " is the correct number")
        break
    x-=1
