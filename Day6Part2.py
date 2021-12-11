file = open('/home/jonob/Forritun/AdventOfCode2021/Day6Input.txt','r')
# file = open('/home/jonob/Forritun/AdventOfCode2021/Day6example1.txt','r')

numberList = [int(num) for num in file.read().split(',') ]
#print(numberList)

school = [0]*9

for num in numberList:
    school[num] +=  1

#print(school)

for days in range(0,256):
    newSchool = [0]*9
    add8 = 0
    for i in range(0, len(school)):
        if i == 0:          
            newSchool[8] += school[i]
            newSchool[6] += school[i]
        else:
            newSchool[i-1] += school[i]
 #   print('After ', days+1,' days:', school)
    school = newSchool.copy()

#print('After ', days+1, ' ' , school)
total = 0
for num in school:
    total += num
print('No. of lanternfish: ', total)            



