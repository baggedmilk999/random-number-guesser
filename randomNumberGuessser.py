import random

randomNum = random.randrange(1,100)

while True:
    guessnum = int(input("GUESS NUMBER 1-100\n"))
    guessnum2 = int(guessnum)

    if guessnum > randomNum:
        print("TOO HIGH") 
    if guessnum < randomNum:
        print("TOO LOW")
    if guessnum == randomNum:
        print("YASSS")
        break