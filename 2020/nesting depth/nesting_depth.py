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
    i = 0

    if len(s) == 1:
        prtss_f = int(s[0])*"("
        prtss_l = int(s[0])*")"
        s_p = prtss_f + s[0] + prtss_l

    else:
        while i<len(s):
            pos = i
            i = i + 1
            if pos == 0:
                prtss = int(s[pos])*"("
                s_p = s_p + prtss + s[pos]
                if s[pos] != s[pos+1]:
                    prtss = int(s[pos])*")"
                    s_p = s_p + prtss
                continue

            if pos == len(s)-1:
                if s[pos] != s[pos-1]:
                    prtss = int(s[pos])*"("
                    s_p = s_p + prtss
                prtss = int(s[pos])*")"
                s_p = s_p + s[pos] + prtss
                continue

            if s[pos] == s[pos+1]:
                if s[pos] == s[pos-1]:
                    s_p = s_p + s[pos]
                else:
                    prtss = int(s[pos])*"("
                    s_p = s_p + prtss + s[pos]
                continue
            else:
                if s[pos] != s[pos-1]:
                    prtss = int(s[pos])*"("
                    s_p = s_p + prtss
                prtss = int(s[pos])*")"
                s_p = s_p + s[pos] + prtss
                continue
            

    print("Case #" + str(testCase) + ": " + s_p)