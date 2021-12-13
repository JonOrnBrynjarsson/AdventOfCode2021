
file = open('/home/jonob/Forritun/AdventOfCode2021/Day8Input.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day8example.txt','r')

all = [line.replace(' -> ',',') for line in file.read().splitlines()]
inputoutput = [l.split(' | ') for l in all]

output = [l[1] for l in inputoutput]

counter =0 
letters = []
for str in output:
    letters.append(str.split(' '))
for ltr in letters:
    for l in ltr:
        if len(l) in (2,3,4,7):
            counter += 1

print(counter)       
#map(int, line.split(',')
#print(inputoutput)
