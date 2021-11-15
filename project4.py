"""
Math 560
Project 4
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
    dp=[[0 for _ in range(0, len(src) + 1)] for _ in range(0,len(dest)+1)]
    prev = [[0 for _ in range(0, len(src) + 1)] for _ in range(0, len(dest) + 1)]
    for i in range(0,len(src) + 1):
        dp[0][i] = i
        if(i<len(src)):
            prev[0][i+1]=('delete',src[i], i)
    for j in range(0,len(dest) + 1):
        dp[j][0] = j
        if (j < len(dest)):
            prev[j+1][0] = ('insert', dest[j], j)
    #print(prev)
    dist = 0  # This is a placeholder, remove and implement!

    edits = []  # This is a placeholder, remove and implement!
    for i in range(1, len(dest) + 1):
        for j in range(1, len(src) + 1):
            minList = []
            if(src[j-1] == dest[i-1]):
                dp[i][j] = dp[i-1][j-1]
                prev[i][j]=('match',src[j - 1],j - 1)
            else:
                minList.append(dp[i-1][j])
                minList.append(dp[i][j-1])
                minList.append(dp[i-1][j-1])
                if minList.index(min(minList)) == 0:
                    prev[i][j] =('insert', dest[j - 1], j)
                elif minList.index(min(minList)) == 1:
                    prev[i][j] =('delete', src[i - 1], j - 1)
                elif minList.index(min(minList)) == 2:
                    prev[i][j] =('sub', dest[i - 1], j - 1)
                else:
                    raise Exception('no min found')
                dp[i][j]=min(minList)+1

    sInd = len(src)
    dInd = len(dest)
    dist = dp[dInd][sInd]
    while(prev[dInd][sInd] != 0):
        opt = prev[dInd][sInd][0]
        edits.append(prev[dInd][sInd])
        if (opt == 'insert'):
            dInd -= 1
        elif (opt == 'delete'):
            sInd -= 1
        elif (opt == 'match' or opt == 'sub'):
            sInd -= 1
            dInd -= 1
    if not src:
        edits.reverse()
    #print(edits)
    #print(dist)
    #print(dp)

    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()

    compareGenomes(True, 30, 300, 'ED')
    print()

    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
