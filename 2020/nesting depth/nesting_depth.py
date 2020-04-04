import sys

name = "nesting_depth"
path = ""

# input and output files (delete if you wanna run in google)
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

# number cases
testCases = int(input())

for testCase in range(1, testCases + 1):
    s = input()
    s_p = ""

    matrix_string = []
    matrix_int = []

    if len(s) == 1:
        matrix_string.append(s)
        matrix_int.append(int(s))
    else:
        for i in range(len(s)):
            if i == 0:
                matrix_string.append(s[i])
                matrix_int.append(int(s[i]))
                continue

            if s[i] != s[i-1]:
                matrix_string.append(s[i])
                matrix_int.append(int(s[i]))
            else:
                matrix_string[-1] = str(matrix_string[-1]) + s[i]


    for i in range(len(matrix_string)):
        if i == 0:
            prtss = matrix_int[i]*"("
            s_p = prtss + matrix_string[i] + s_p
        
        else:
            # Calculate parentheses
            prtss_value = matrix_int[i] - matrix_int[i-1]
            if prtss_value > 0:
                prtss =prtss_value*"("
            else:
                prtss = (prtss_value*-1)*")"
            s_p = s_p + prtss + matrix_string[i]

        if i == len(matrix_string)-1:
            prtss = matrix_int[i]*")"
            s_p = s_p + prtss

            

    print("Case #" + str(testCase) + ": " + s_p)