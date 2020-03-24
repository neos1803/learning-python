import random

wordList = [
    "am",
    "an",
    "uw",
    "er",
    "ap",
]

guessedList = []

chance = 2

n = input("Do you want to play the game? Y to continue N to exit ").upper()

if n == "Y":
    guessedWord = list(random.choice(wordList))
    blankWord = guessedWord
    print(blankWord)
    for w in guessedWord:
        print("_ ", end=" ")
    
    while chance > 0:
        print(blankWord)
        if len(blankWord) == 0:
            print("Congrats, you have guess the word: ", guessedWord)
            break
        else:
            s = input("\nGuess the word: ")
            if s in guessedList:
                print("Ooops you have guess the word!")
            else:
                guessedList.append(s)
                if s in guessedWord:
                    guessedWord = guessedWord.remove(s)
                    print("You got the word")
                else:
                    print("Ooops, seems you guess it wrong")
        chance-=1
else:
    print("Goodbye!")
