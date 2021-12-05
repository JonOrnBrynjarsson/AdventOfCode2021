f = open('/home/jonob/Forritun/AdventOfCode2021/Day1Input1.txt','r')
#f = open('/home/jonob/Forritun/AdventOfCode2021/Day1example1.txt','r')


num1 = int(f.readline(500).strip('\n'))
num2 = int(f.readline(500).strip('\n'))
counter = 0
currLine = 1

dictSum = {}
for i in f:
    num3 = int(i.strip('\n'))
    dictSum[currLine] = num1+num2+num3
    num1 = num2
    num2 = num3
    currLine += 1

#currLine = 1
prevSum = 0
print(len(dictSum))
for d in range(1, len(dictSum)+1):
    if d > 1:
        print(dictSum[d], ' >' , prevSum)
        if dictSum[d] > prevSum:
            counter += 1
        prevSum = dictSum[d]
    else:
        prevSum = dictSum[d]
print(counter)

