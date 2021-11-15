"""
Math 560
Project 4
Fall 2021

Partner 1: Harrison Hao-Yu Ku hk261
Partner 2: Ping-Cherng Lin pl204
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

    dist = 0
    edits = []

    # base_case = []
    # if prob == 'ED':
    #     base_case = [('insert', k) for k in range(len(dest) + 1)]
    # else:
    #     base_case = [('insert', 0) for k in range(len(dest) + 1)]
    base_case = [('insert', k) if prob == 'ED' else ('insert', 0) for k in range(len(dest) + 1)]
    ED_table = [base_case]

    for i in range(1, len(src) + 1):
        row = [('delete', ED_table[i-1][0][1] + 1)]
        
        for j in range(1, len(dest) + 1):
            if src[i-1] == dest[j-1]:
                row.append(('match', ED_table[i-1][j-1][1]))
            else:
                # print(f'i: {i}, j: {j}')

                action = min(ED_table[i-1][j-1][1], ED_table[i-1][j][1], row[j-1][1])
                
                # if action == ED_table[i-1][j-1][1]:
                #     row.append(('sub', action + 1))
                # elif action == ED_table[i-1][j][1]:
                #     row.append(('delete', action + 1))
                # else:
                #     row.append(('insert', action + 1))
                if action == row[j-1][1]:
                    row.append(('insert', action + 1))
                elif action == ED_table[i-1][j][1]:
                    row.append(('delete', action + 1))
                else:
                    row.append(('sub', action + 1))
        
        ED_table.append(row)

    dist = ED_table[len(src)][len(dest)][1]

    i = len(src)
    j = len(dest)
    
    while i > 0 or j > 0:
        if ED_table[i][j][0] == 'match':
            edits.append(('match', src[i-1], i - 1))
            i -=1
            j -=1
        elif ED_table[i][j][0] == 'sub':
            edits.append(('sub', dest[j-1], i - 1))
            i -=1
            j -=1
        elif ED_table[i][j][0] == 'insert':
            edits.append(('insert', dest[j-1], i))
            j -=1
        else:
            edits.append(('delete', src[i-1], i - 1))
            i -=1

        if j == 0 and prob == 'ASM':
            break

    #print(edits)
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    '''
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
'''