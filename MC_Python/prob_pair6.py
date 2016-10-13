import random

def rollDie(): 
 """returns a random int between 1 and 6""" 
 return random.choice([1,2,3,4,5,6])

def Monteprob(numTrials): 
    numwins = 0.0 
    for i in range(numTrials): 
        for j in range(24): 
            d1 = rollDie() 
            d2 = rollDie() 
            if d1 == 6 and d2 == 6: 
                numwins += 1 
                break 
    print(numwins/numTrials) 
