
# guess small game to find number Secret 
# the program you ask to give them the range of numbers to check
# in this game we use random to return a random Number


import random


def guess ():
    x = int(input("give me the max number\n"))
    randomNumber = random.randint(0,x)
    countEssay = 1
    numberUser = -1
    while randomNumber != numberUser:
        numberUser = int(input(F"give me the secret Number between 0 and {x}\n"))
        if randomNumber > numberUser:
            print(f"the secret number is high than {numberUser}")
        elif randomNumber < numberUser:
            print(f"the secret number is less than {numberUser}")
        else:
            print(f"the secret number is egual to {numberUser}")
            print(f"you are found number after  {countEssay} essay")
        countEssay+=1

            

guess()
