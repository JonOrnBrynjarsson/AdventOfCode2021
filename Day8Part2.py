
def stringlenght(elem):
    return len(elem)

def getNumber(letter, Board):
    if len(letter) == 2: return '1'
    elif len(letter) == 4: return '4'
    elif len(letter) == 3: return '7'
    elif len(letter) == 7: return '8'
    elif len(letter) == 5:
        if  letter.find(Board[2]) == -1 and letter.find(Board[1]) == -1:
            return '3'
        elif letter.find(Board[2]) == -1: return '5'
        elif letter.find(Board[1]) == -1 : return '2'
        else: return '-1'
    else :
        if letter.find(Board[4]) == -1: return '0'
        elif letter.find(Board[1]) >-1 and letter.find(Board[2]) > -1:
            return '6'
        else: return '9'

file = open('/home/jonob/Forritun/AdventOfCode2021/Day8Input.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day8example.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day8exampleSimple.txt','r')


inputoutput = [l.split(' | ') for l in file.read().splitlines()]

output = [l[1] for l in inputoutput]
input = [l[0] for l in inputoutput]


boardList = []

letters = []
for str in input:
    letters.append(sorted(str.split(' '),key=stringlenght))
    for ltr in letters:
        numboard = {1:'',2:'',3:'',4:'',5:'',6:'',7:''}
        ltr = [''.join(sorted(l)) for l in ltr ]
        # Working with 1
        numboard[6] = ltr[0]
        numboard[7] = ltr[0]
        # Working with 7
        numboard[3] = ltr[1].replace(ltr[0][0],'').replace(ltr[0][1],'') 
        # Working with 4
        numboard[4] = ltr[2].replace(ltr[0][0],'').replace(ltr[0][1],'') 
        numboard[1] = numboard[4]
        # Working with 8
        numboard[2] = ltr[9].replace(ltr[0][0],'').replace(ltr[0][1],'')
        numboard[2] = numboard[2].replace(numboard[3],'').replace(numboard[1][0],'').replace(numboard[1][1],'')
        numboard[5] = numboard[2]

        # Working with 3
        tmp3 = ''
        if ltr[3].find(numboard[6][0]) > -1 and ltr[3].find(numboard[6][1])  > -1:
            tmp3 = ltr[3].replace(ltr[0][0],'').replace(ltr[0][1],'') 
        elif ltr[4].find(numboard[6][0]) > -1 and ltr[4].find(numboard[6][1]) > -1:
            tmp3 = ltr[4].replace(ltr[0][0],'').replace(ltr[0][1],'') 
        else:
            tmp3 = ltr[5].replace(ltr[0][0],'').replace(ltr[0][1],'') 
        #remove the topline
        tmp3 = tmp3.replace(numboard[3],'')
        #Middleline and bottomline
        if numboard[4].find(tmp3[0]) > -1: 
            numboard[4] = tmp3[0]
            numboard[5] = tmp3[1]
        else:
            numboard[4] = tmp3[1]
            numboard[5] = tmp3[0]
        #Clean up
        numboard[2] = numboard[2].replace(numboard[5],'')
        numboard[1] = numboard[1].replace(numboard[4],'')

    boardList.append(numboard)


letters = []
resultString = []
for str in range(0,len(output)):
    letters.append(output[str].split(' '))
    letter = letters[str]
    tmpltr = []
    for ltr in letter:
        board = boardList[str]
        tmpltr.append(getNumber(ltr,boardList[str]))
    resultString.append(tmpltr)

resultnumer = 0
for num in resultString:
    nStr = ''.join(num)
    resultnumer += int(nStr)
print(resultnumer)

