f = open('/home/jonob/Forritun/AdventOfCode2021/Day1Input1.txt','r')
#f = open('/home/jonob/Forritun/AdventOfCode2021/Day1example1.txt','r')

#print(f.read())

firstnum = int(f.readline(500).strip('\n'))
counter = 0
for i in f:
    if int(i.strip('\n')) > firstnum:        
        counter += 1
    firstnum = int(i.strip('\n'))
print(counter)
    