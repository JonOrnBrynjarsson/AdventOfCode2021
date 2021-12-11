from collections import Counter

file = open('/home/jonob/Forritun/AdventOfCode2021/Day5Input1.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day5example1.txt','r')

all = [line.replace(' -> ',',') for line in file.read().splitlines()]

maxhint = 0
minhnit = 10000
cords = []

for line in all:
    x1, y1, x2, y2 = map(int, line.split(','))
    (x1,y1),(x2,y2) = sorted([(x1,y1),(x2,y2)])    
    if x1 == x2 or y1 == y2:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                cords.append((x,y))
    #part2                
    else:
        Add = 1
        if y2 > y1:
            Add = 1
        else: 
            Add = -1
        y = y1
        
        for x in range(x1, x2+1):
                cords.append((x,y))
                y += Add

cords.sort()

MoreThanOne =  [p for p in Counter(cords).values() if p > 1]
print ('Svarið er: ', len(MoreThanOne))
