
def ChangeToBits(filelength,textlength, list):
    retList = [''] * textlength
    for ltr in range(0, len(list)):
        if list[ltr] > (filelength / 2):
            retList[ltr] = '1'
        else:
            retList[ltr] = '0'
    return ''.join(retList)


file = open('/home/jonob/Forritun/AdventOfCode2021/Day3Input1.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day3example1.txt','r')

filelen = sum(1 for line in file)
file.seek(0)
textlen = len(file.readline(500).strip('\n'))

#print(textlen)
oneList = [0] * textlen
zeroList = [0] * textlen
file.seek(0)

for line in file:
    lineString = line.strip('\n')    
    for ltr in range(0, len(lineString)):                
        if(int(lineString[ltr]) == 1):
            oneList[ltr] += 1
        else:  
            zeroList[ltr] += 1
        
#print(oneList)
#print(zeroList)


gammaRate = ChangeToBits(filelen, textlen, oneList)
epsilonRate = ChangeToBits(filelen, textlen, zeroList)


print(oneList, zeroList, int(gammaRate, 2), int(epsilonRate,2), int(gammaRate, 2)*int(epsilonRate,2))
