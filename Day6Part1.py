#file = open('/home/jonob/Forritun/AdventOfCode2021/Day6Input.txt','r')
file = open('/home/jonob/Forritun/AdventOfCode2021/Day6example1.txt','r')

numberList = [int(num) for num in file.read().split(',') ]
print(numberList)

for days in range(0,12):
    addlist = []
    for i in range(0, len(numberList)):
        num = numberList[i]
        if num == 0:
            numberList[i] = 6 
            addlist.append(8)        
        else:
            numberList[i] = num-1
    [numberList.append(num) for num in addlist]    
    print('After ', days+1, ' ' , numberList)
print('No. of lanternfish: ', len(numberList))


