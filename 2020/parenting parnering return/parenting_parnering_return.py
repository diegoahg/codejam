import sys

name = "parenting_parnering_return"
path = ""

# input and output files (delete if you wanna run in google)
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

# number cases
testCases = int(input())

# Take first for List sort
def takeFirst(elem):
    return elem[0]

# Return position of couple not busy, if all are busy return -1
def getNotBusy(couple, time):
    for i in range(len(couple)):
        if couple[i][1] == 0 or couple[i][1] <= time:
            return i
    return -1

# Return schedule according of the couple
def GenerateSchedule(schdle):
    schdle.sort(key=takeFirst)
    couple = [["C",0], ["J", 0]]
    for i in range(len(schdle)):
        if i == 0:
           couple[0][1] = schdle[i][1]
           schdle[i].append(couple[0][0])
           continue
        
        not_busy = getNotBusy(couple, schdle[i][0])
        if not_busy == -1:
            return -1
        else:
            couple[not_busy][1] = schdle[i][1]
            schdle[i].append(couple[not_busy][0])
    return schdle

# Return output of the problem
def GenerateOutput(schdle):
    y = ""
    for i in range(len(schdle)):
        y = y + schdle[i][2]

    return y

for testCase in range(1, testCases + 1):
    n = int(input())
    schdle = []
    schdle_p = []
    for i in range(n):
        tupla = input().split()
        tupla[0], tupla[1] = int(tupla[0]), int(tupla[1])
        schdle.append(tupla)
        schdle_p.append(tupla)

    # sort list with key
    schdle_p = GenerateSchedule(schdle_p)
    y = "IMPOSSIBLE"
    if schdle_p != -1:
        y = GenerateOutput(schdle)
            
    print("Case #" + str(testCase) + ": " + y)