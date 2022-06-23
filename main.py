# Create an array where the array[index] contains the factorial of index-1
import math
import time
package = 'matplotlib'
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib is not installed. You can install it by running 'pip install matplotlib'")



#Recursive Function for Top-Down Algorithm
def recursivePaths(y, x, turnsLeft, direction, arrayPaths):

    #If we are going too far, return 0
    if (y < 0 or x < 0):
        return 0
    #If we reached point P_0(0,0), return 1 cause we found a path
    if (y == 0 and x == 0):
        return 1

    #If we have 0 turns left
    if (turnsLeft == 0):
        # If direction is row, then we can reach here
        # only if direction is row and row is 0.
        #If we are going left, and we stay on the first row, we can reach P_0(0,0) without consuming any turns
        if (direction == 0 and y == 0):
            return 1
        #If we are going up, and we stay on the first column, we can reach P_0(0,0) without consuming any turns
        if (direction == 1 and x == 0):
            return 1
        #Otherwise, we can't reach P_0(0,0)
        return 0

    #If the problem was already solved, then
    if (arrayPaths[y][x][turnsLeft][direction] != -1):
        return arrayPaths[y][x][turnsLeft][direction]

    #If we are going left
    if (direction == 0):
        arrayPaths[y][x][turnsLeft][direction] = recursivePaths(y, x - 1, turnsLeft, direction, arrayPaths) + \
                                                 recursivePaths(y - 1, x, turnsLeft - 1, not direction, arrayPaths)
        return arrayPaths[y][x][turnsLeft][direction]
    #Else if we are going up
    arrayPaths[y][x][turnsLeft][direction] = recursivePaths(y - 1, x, turnsLeft, direction, arrayPaths) + \
                                                 recursivePaths(y, x - 1, turnsLeft - 1, not direction, arrayPaths)

    return arrayPaths[y][x][turnsLeft][direction]


#Main function to count all possible paths with at most k turns using top-down algorithm
def countPathTopDown(n, k):
    # If (0, 0) is target itself
    if (n == 0):
        return 0
    lenght = max(n, k)
    array = [[[[-1 for col in range(2)]
            for col in range(lenght + 1)]
           for row in range(lenght)]
          for row in range(lenght)]
    # Recur for two cases: moving along row
    # and along column

    return recursivePaths(n - 2, n-1, k, 1, array) + recursivePaths(n-1, n - 2, k, 0, array)

#Creates an array with all the factorials from 0 to n
def createFactorialArray(z):  # O(n)
    factorials = [1] * (z+1)
    for i in range(1, z+1):
        factorials[i] = factorials[i - 1] * i
    return factorials

#Main function to count all possible paths with at most k turns using combinatoric algorithm (or bottom-up algorithm)
def countPaths(n: int, k: int): #O(k)
    finalCount = 0
    if (n < 2):
        return 0
    if k>=2*n-3:
        return int(math.factorial(2*n-2) / (math.factorial(n-1) * math.factorial(n-1)))
    else:
        factorials = createFactorialArray(n - 2)
        for i in range(1, k+1):
            finalCount += 2 *\
                            (int((factorials[n - 2]) / (factorials[math.floor(i / 2)] *
                            factorials[(n-2) - math.floor(i / 2)]))) * \
                            (int((factorials[n - 2]) / (factorials[math.floor((i - 1) / 2)] *
                            factorials[(n-2) - math.floor((i - 1) / 2)])))
    return finalCount


# With a grid n*n, count all possible paths with at most k turns
def printPathsCA(n, k):
    print(countPaths(n, k))

def printPathsTD(n, k):
    print(countPathTopDown(n,k))


def showChartCA(numberOfElement, k):
    tries = numberOfElement
    times = list()
    elements = list()
    times2 = list()
    elements2=list()
    elements3=list()
    times3=list()

    for i in range(0,tries):
        n = i
        start = time.perf_counter()
        countPaths(n, k)
        end = time.perf_counter()
        elements.append(n)
        times.append(end-start)

        """
        For plotting Top-Down Algorithm
        start = time.perf_counter()
        countPathTopDown(n, k)
        end = time.perf_counter()
        elements3.append(n)
        times3.append(end-start)
        """

    for i in range(0,tries):
        elements2.append(1 * i)
        times2.append(0.000001 * i)

    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.plot(elements, times, label='Combinatoric Algorithm O(n)')
    plt.plot(elements2, times2, label='O(n)')
    """
    For plotting Top-Down Algorithm
    plt.plot(elements3, times3, label='Top-Down Algorithm O(n\u00b2k)')
    """
    plt.grid()
    plt.legend()
    plt.show()

def showChartWithTD(numberOfElement, k):
    tries = numberOfElement
    times = list()
    elements = list()
    times2 = list()
    elements2=list()
    elements3=list()
    times3=list()

    for i in range(0,tries):
        n = i
        start = time.perf_counter()
        countPaths(n, k)
        end = time.perf_counter()
        elements.append(n)
        times.append(end-start)


        start = time.perf_counter()
        countPathTopDown(n, k)
        end = time.perf_counter()
        elements3.append(n)
        times3.append(end-start)


    for i in range(0,tries):
        elements2.append(1 * i)
        times2.append(0.000001 * i)

    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.plot(elements, times, label='Combinatoric Algorithm O(n)')
    plt.plot(elements2, times2, label='O(n)')


    plt.plot(elements3, times3, label='Top-Down Algorithm O(n\u00b2k)')

    plt.grid()
    plt.legend()
    plt.show()
    pass

"""
n = 35
k = 2
printPathsTD(n,k)
printPathsCA(n,k)

"""