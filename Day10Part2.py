def finishOff(Open, Score):
    if not Open: return Score/5
    currSign = Open.pop()
    newScore = 0
    if currSign == '(': newScore = (Score + 1) * 5
    elif currSign == '[': newScore = (Score + 2) * 5
    elif currSign == '{': newScore = (Score + 3) * 5
    elif currSign == '<': newScore = (Score + 4) * 5
    else: return -1
    return finishOff(Open, newScore)

def recurseCheck(Open, Left, Score):
    if not Left: return finishOff(Open, 0) # No more brackets left ( incomplete)
    currSign = Left[0]
    if currSign in ('(','[','{','<'):
        Open.append(currSign)
        Left1 = Left.replace(currSign, '', 1)
        return recurseCheck(Open, Left1, Score)
    elif currSign in (')',']','}','>'):
        checkOpen = Open.pop()
        if ((checkOpen == '(' and currSign == ')') or 
            (checkOpen == '[' and currSign == ']') or 
            (checkOpen == '{' and currSign == '}') or 
            (checkOpen == '<' and currSign == '>')):
            Left1 = Left.replace(currSign, '', 1)
            return recurseCheck(Open, Left1, Score)
        else:
            return 0            
            #if currSign == ')': return 3
            #elif currSign == ']': return 57
            #elif currSign == '}': return 1197
            #elif currSign == '>': return 25137
            #else: return -1
            
    else: return -1



file = open('/home/jonob/Forritun/AdventOfCode2021/Day10Input.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day10example.txt','r')

io = file.read().splitlines()

#print(io)


Left = []

totalScore = []
for line in io:    
    Open = []
    currScore = recurseCheck(Open, line, 0)
 #   print(currScore)
    totalScore.append(currScore)
totalScore.sort()
totalScore = [i for i in totalScore if i != 0]

#for item in range(len(totalScore)-1, 0,-1):
#    if totalScore(item) == 0: totalScore.pop(item)
lenlist = int((len(totalScore) -1)/2)

print(totalScore[lenlist])

