from random import randint

message = """
Welcome to Guess The Number game

The rules are simple
1) Enter how many chance do you want to try, from 1 to 10
2) The number you need to guess is randomly selected from 50 to 50
3) Happy guessing
"""
x = int(input("How many chances do you want? "))
trueNumber = randint(0, 50)

if x < 0 or x > 10:
    print("Invalid number of chance. You enter", x)
else:
    while (x > 0):
        print("You have ", x, " chance")
        n = int(input("Guess the number: "))

        if n > trueNumber :
            print("You need to guess lower!\n")
        elif n < trueNumber :
            print("You need to guess higher!\n")
        else :
            print("You guess it right, ", trueNumber, " is the correct number")
            break
        x-=1
    print("You have no chance left")
