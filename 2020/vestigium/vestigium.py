import sys

name = "vestigium"
path = ""

# input and output files (delete if you wanna run in google)
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

# number cases
testCases = int(input())

# Verify if exists dumplicate values
def values_duplicated(lista):
    return list(set([k for k in lista if lista.count(k)>1]))

for testCase in range(1, testCases + 1):
    n = int(input())
    matrix = [[0 for i in range(n)] for y in range(n)] 
    k, r, c = 0, 0, 0
    for i in range(n):
        row = input().split()
        for j in range(len(row)):
            matrix[j][i] = row[j]

            # Calculate diagonal sum
            if i == j:
                k = int(row[j]) + k

        # Verify dumplicates in rows
        if values_duplicated(row):
                r = r + 1

    # Verify dumplicates in columns
    for i in range(len(matrix)):
        if values_duplicated(matrix[i]):
                c = c + 1

    print("Case #" + str(testCase) + ": " + str(k) + " " + str(r) + " " + str(c))