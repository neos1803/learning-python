import random

myList = ["Rock", "Paper", "Scissor"]
n = int(input("Best of (3/5/7) : "))
if n != 5 and n != 3 and n != 7:
    print("Please input 3, 5 or 7")
else :
    yourScore = 0
    botScore = 0
    while yourScore + botScore < n:
        rdm = random.choice(myList)
        if n == 3 and yourScore == 2 or botScore == 2:
            break
        elif n == 5 and yourScore == 3 or botScore == 3:
            break
        elif n == 7 and yourScore == 5 or botScore == 5:
            break
        else:
            guess = input("Rock/Paper/Scissor : ")
            if guess != rdm:
                if guess == "Rock" and rdm == "Paper":
                    botScore+=1
                    print(guess + " lose to " + rdm, yourScore, "-", botScore)
                elif guess == "Rock" and rdm == "Scissor":
                    yourScore+=1
                    print(guess + " win against " + rdm, yourScore, "-", botScore)
                elif guess == "Paper" and rdm == "Rock":
                    yourScore+=1
                    print(guess + " win against " + rdm, yourScore, "-", botScore)
                elif guess == "Paper" and rdm == "Scissor":
                    botScore+=1
                    print(guess + " lose againts " + rdm, yourScore, "-", botScore)
                elif guess == "Scissor" and rdm == "Paper":
                    yourScore+=1
                    print(guess + " win against " + rdm, yourScore, "-", botScore)
                elif guess == "Scissor" and rdm == "Rock":
                    botScore+=1
                    print(guess + " lose to " + rdm, yourScore, "-", botScore)
            else:
                print("Draw, ", yourScore, "-", botScore)       
    if yourScore < botScore:
        print("You Lose")
    else:
        print("You Win")
