import random
#number genrator for numtesr


#difficulty can be set using many
def NumGen(difficulty:int):
    low = "1" + "0"*difficulty
    low = int(low)
    high  = "9" + "9"*difficulty
    high  = int(high)

    number = random.randint(low,high)
    return number
