file = open('/home/jonob/Forritun/AdventOfCode2021/Day2Input1.txt','r')
#file = open('/home/jonob/Forritun/AdventOfCode2021/Day2example1.txt','r')

vertical = 0
horizontal = 0

for line in file:
    tuple = line.split()
    if tuple[0] == 'forward':
        horizontal += int(tuple[1])
    elif tuple[0] == 'down':
        vertical += int(tuple[1])
    elif tuple[0] == 'up':
        vertical -= int(tuple[1])


print(vertical*horizontal)
