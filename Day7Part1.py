from collections import Counter

def fuelCalc(disance):
    retvalue = 0
    for i in range(1,disance+1):
        retvalue += i
    return retvalue




file = open('/home/jonob/Forritun/AdventOfCode2021/Day7Input.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day7example.txt','r')

numberList = [int(num) for num in file.read().split(',') ]
#print(numberList)

maxNum = max(numberList)
#print(maxNum)

BestPos = -1
BestCost = maxNum**len(numberList)


for checkPos in range(1,maxNum+1):
    currCost = 0
    for i in numberList:
        currCost += fuelCalc(abs( checkPos - i)) #part2
        #currCost += abs( checkPos - i) #part1
    if currCost < BestCost:
        #print('Currnum: ', i)
        BestCost = currCost 
        BestPos = checkPos
    if checkPos == 10:
        print('cost of 2 ',currCost)

print('Best pos: ',BestPos, ' and totalCost: ', BestCost )

