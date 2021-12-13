file = open('/home/jonob/Forritun/AdventOfCode2021/Day9Input.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day9example.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day9exampleSimple.txt','r')

io = file.read().splitlines()
#print(io)

#print(str(io[0]).replace('\'','').replace('\[','').replace('\]',''))
Width = len(str(io[0]).replace('\'',''))
print(io)


LowpointRisk = 0

for lnr in range(0, len(io)):
    
    #lowpoint = True
    for currPos in range(0,Width):
        if currPos == 9: 
            print('')
        currNum = io[lnr][currPos]
        if lnr > 0 and currNum >= io[lnr-1][currPos]:
            continue
        elif lnr < len(io)-1 and currNum >= io[lnr+1][currPos]:
            continue
        elif currPos > 0 and currNum >= io[lnr][currPos-1]:
            continue
        elif currPos < Width-1 and  currNum >= io[lnr][currPos+1]:
            continue
        else:
            print(currNum)
            LowpointRisk += int(currNum) + 1

print('total ', LowpointRisk)
    

