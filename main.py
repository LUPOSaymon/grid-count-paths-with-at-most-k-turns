# Create an array where the array[index] contains the factorial of index-1
import math
import time
import matplotlib.pyplot as plt




# Returns count of paths to reach
# (i, j) from (0, 0) using at-most k turns.
# d is current direction, d = 0 indicates
# along row, d = 1 indicates along column.
def countPathsUtil(i, j, k, d,dp):
    # If invalid row or column indexes
    if (i < 0 or j < 0):
        return 0

    # If current cell is top left itself
    if (i == 0 and j == 0):
        return 1

    # If 0 turns left
    if (k == 0):

        # If direction is row, then we can reach here
        # only if direction is row and row is 0.
        if (d == 0 and i == 0):
            return 1

        # If direction is column, then we can reach here
        # only if direction is column and column is 0.
        if (d == 1 and j == 0):
            return 1

        return 0

    # If this subproblem is already evaluated
    if (dp[i][j][k][d] != -1):
        return dp[i][j][k][d]

    # If current direction is row,
    # then count paths for two cases
    # 1) We reach here through previous row.
    # 2) We reach here through previous column,
    # so number of turns k reduce by 1.
    if (d == 0):
        dp[i][j][k][d] = countPathsUtil(i, j - 1, k, d,dp) + \
                         countPathsUtil(i - 1, j, k - 1, not d,dp)
        return dp[i][j][k][d]

    # Similar to above if direction is column
    dp[i][j][k][d] = countPathsUtil(i - 1, j, k, d,dp) + \
                     countPathsUtil(i, j - 1, k - 1, not d,dp)
    return dp[i][j][k][d]


# This function mainly initializes 'dp' array
# as -1 and calls countPathsUtil()
def countPaths2(i, j, k,MAX):
    # If (0, 0) is target itself
    if (i == 0 and j == 0):
        return 1
    dp = [[[[-1 for col in range(2)]
            for col in range(MAX+1)]
           for row in range(MAX+1)]
          for row in range(MAX+1)]
    # Recur for two cases: moving along row
    # and along column
    return countPathsUtil(i - 1, j, k, 1,dp) + \
           countPathsUtil(i, j - 1, k, 0,dp)

def createFactorialArray(z):  # O(n)
    factorials = [1] * (z+1)
    for i in range(1, z+1):
        factorials[i] = factorials[i - 1] * i
    return factorials


def countPaths(n: int, k: int, factorials: []): #O(k)
    finalCount = 0
    for i in range(1, k+1):
        finalCount += 2 *   \
                        (   int((factorials[n - 2]) / (factorials[math.floor(i / 2)] * factorials[(n-2) - math.floor(i / 2)]))) * \
                        (   int((factorials[n - 2]) / (factorials[math.floor((i - 1) / 2)] * factorials[(n-2) - math.floor((i - 1) / 2)]))   )
    return finalCount


# With a grid n*n, count all possible paths with at most k turns
def printPaths(n, k):
    factorials = createFactorialArray(n - 2)
    count = countPaths(n, k, factorials)
    print(count)






def printChart():
    k = 4
    times = list()
    elements = list()
    times2 = list()
    elements2=list()
    for i in range(k,200):
        n = i
        start = time.perf_counter()
        factorials = createFactorialArray(n - 2)
        countPaths(n, k, factorials)
        end = time.perf_counter()
        elements.append(n)
        times.append(end-start)

        start = time.perf_counter()
        MAX = n
        countPaths2(n-1,n-1,k,MAX)
        end = time.perf_counter()
        times2.append(end-start)
        elements2.append(n)

    plt.xlabel('n')
    plt.ylabel('Time')
    plt.plot(elements, times, label='Actual Time')
    plt.plot(elements2,times2,label="Count")
    plt.grid()
    plt.legend()
    plt.show()
    pass

printChart()