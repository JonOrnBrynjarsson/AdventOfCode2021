#def checkSign

def recurseCheck(Open, Left, Score):
    if not Left: return 0    
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
            if currSign == ')': return 3
            elif currSign == ']': return 57
            elif currSign == '}': return 1197
            elif currSign == '>': return 25137
            else: return -1
    else: return -1









file = open('/home/jonob/Forritun/AdventOfCode2021/Day10Input.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day10example.txt','r')

io = file.read().splitlines()

print(io)

Open = []
Left = []

totalScore = 0
for line in io:    
    currScore = recurseCheck(Open, line, 0)
    print(currScore)
    totalScore += currScore

print(totalScore)


