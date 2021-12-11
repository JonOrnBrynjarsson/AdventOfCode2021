def CheckIfWinner(Board):    
    for line in Board:
        linesum = sum(line)
        #print(linesum)
        if linesum == 5:
            return True
    for item in range(0,5):
        colsum = 0
        for line in Board:
            if line[item] == 1:
                colsum += 1
        if colsum == 5:
            return True
    return False


#file = open('/home/jonob/Forritun/AdventOfCode2021/Day4Input1.txt','r')
file = open('/home/jonob/Forritun/AdventOfCode2021/Day4example1.txt','r')

all = file.read().splitlines()
numbers = all[0]
all.pop(1)
all.pop(0)

oneboard = []
boards = []

for line in all:
    if line == '':
        boards.append(oneboard)
        oneboard = []
        continue
    oneboard.append(line.split())
boards.append(oneboard)

#Búum til fylki sem heldur utan um vinnings tölurnar
winnerBoard = []
currentBoardCount = [[0 for y in range(5)] for x in range(5)]
winnerBoardCount = [[0 for y in range(5)] for x in range(5)]
winnerCount = 100
currentCount = int
winningNum = int
winningBaordNr = 0
boardnr = 0


for checkboard in boards:
    boardnr += 1
    if boardnr == 8:           
        print('ath')
    currentCount = 0
    currentBoardCount = [[0 for y in range(5)] for x in range(5)]
    for num in numbers.split(','):
        currentCount += 1
        if(CheckIfWinner(currentBoardCount)):
            break
    #for board in boards:
        for x in range(0, 5):
            if(CheckIfWinner(currentBoardCount)):
                break
            for y in range(0, 5):
                if(CheckIfWinner(currentBoardCount)):
                    break
                if checkboard[x][y] == num:
                    
                    currentBoardCount[x][y] = 1
                    if(CheckIfWinner(currentBoardCount)):
                        if currentCount < winnerCount: 
                            if boardnr == 8:           
                                print('ath')
                            winnerCount = currentCount
                            winnerBoardCount = currentBoardCount
                            winnerBoard = checkboard
                            winningNum = num
                            winningBaordNr = boardnr
    print('nr. ', boardnr, ' Winningnum: ', num, ' Count: ', currentCount)
    
            
    
#Next up multiplying to get the marked numbers
resultboard = [[0 for y in range(5)] for x in range(5)]
for i in range(0,len(winnerBoard)):
    print(winnerBoard[i])
for i in range(0,len(winnerBoardCount)):
    print(winnerBoardCount[i])



for i in range(len(winnerBoardCount)):
   for j in range(len(winnerBoardCount[i])):
        resultboard[i][j] = winnerBoardCount[i][j] * int(winnerBoard[i][j])
print('Next up the result')
print(resultboard)

#summing the marked numbers
intMarkedNums = 0
for i in range(len(resultboard)):
   for j in range(len(resultboard[i])):
       intMarkedNums += resultboard[i][j]

intAllNums = 0
for i in range(len(winnerBoard)):
   for j in range(len(winnerBoard[i])):
       intAllNums += int(winnerBoard[i][j])
Answer = int(intAllNums-intMarkedNums) * int(winningNum)
print('result is: ', Answer, ' and board nr. ', winningBaordNr)

