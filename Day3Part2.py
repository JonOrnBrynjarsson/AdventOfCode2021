file = open('/home/jonob/Forritun/AdventOfCode2021/Day3Input1.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day3example1.txt','r')

oxygenList = file.read().splitlines()
co2scrubList = oxygenList.copy()
textlen = len(oxygenList[0])

#Skoðum Oxygen  (Could be extracted)
for ltr in range(0,textlen):
    counter = 0
    if len(oxygenList) == 1:
        print(oxygenList)
    else:
        for line in oxygenList:
            if line[ltr] == '1':
                counter += 1
        if counter >= len(oxygenList)/2:
            for line in range(len(oxygenList)-1, -1, -1):
                if oxygenList[line][ltr] == '0':
                    print(line, ltr, oxygenList[line][ltr] , "- - ", oxygenList[line])
                    oxygenList.pop(line)
        else:
            for line in range(len(oxygenList)-1, -1, -1):
                if oxygenList[line][ltr] == '1':
                    oxygenList.pop(line)

#Skoðum Co2                    
for ltr in range(0,textlen):
    counter = 0
    if len(co2scrubList) == 1:
        print(co2scrubList)
    else:
        for line in co2scrubList:
            if line[ltr] == '1':
                counter += 1
        if counter < len(co2scrubList)/2:
            for line in range(len(co2scrubList)-1, -1, -1):
                if co2scrubList[line][ltr] == '0':
                    print(line, ltr, co2scrubList[line][ltr] , "- - ", co2scrubList[line])
                    co2scrubList.pop(line)
        else:
            for line in range(len(co2scrubList)-1, -1, -1):
                if co2scrubList[line][ltr] == '1':
                    co2scrubList.pop(line)    
        
oxygenInt = int(oxygenList[0],2)
co2Int = int(co2scrubList[0],2)
print(oxygenList, co2scrubList, oxygenInt, co2Int, oxygenInt * co2Int)
