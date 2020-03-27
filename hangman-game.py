import random

wordList = [
    "chimp",
    "urban",
    "dine",
    "come",
    "bonfire",
]

guessedList = []

chance = 5
wrongAttempt = 0

n = input("Do you want to play the game? Y to continue N to exit ").upper()

if n == "Y":
    guessedWord = list(random.choice(wordList))
    blankWord = guessedWord.copy()
    for w in guessedWord:
        print("_ ", end=" ")
    
    while chance > 0:
        if len(blankWord) == 0:
            print("Congrats, you have guess the word")
            for w in guessedWord:print(w, end="")
            break
        else:
            s = input("\nGuess the word: ")
            if s in guessedList:
                print("Ooops you have guess the word!")
                chance+=1
            else:
                guessedList.append(s)
                if s in blankWord:
                    blankWord.remove(s)
                    print("You got the word")
                    chance+=1
                else:
                    print("Ooops, seems you guess it wrong")
                    wrongAttempt+=1
                    if wrongAttempt == 1:
                        print("--")
                    elif wrongAttempt == 2:
                        print("""
                            ____
                                |
                                O

                        """)
                    elif wrongAttempt == 3:
                        print("""
                            ____
                                |
                                O
                                |

                        """)
                    elif wrongAttempt == 4:
                        print("""

                            ____
                                |
                                O
                               /|\\

                        """)
                    elif wrongAttempt == 5:
                        print("""

                            ____
                                |
                                O
                               /|\\
                               / \\

                        """)
        chance-=1
    
else:
    print("Goodbye!")
