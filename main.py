# Create an array where the array[index] contains the factorial of index-1
import math
import time
import matplotlib.pyplot as plt

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



n= 35
k=11
printPaths(n,k)


def printChart():
    k = 4
    times = list()
    elements = list()
    for i in range(k,10000):
        n = i
        start = time.process_time()
        factorials = createFactorialArray(n - 2)
        countPaths(n, k, factorials)
        end = time.process_time()
        elements.append(n)
        times.append(end-start)

    plt.xlabel('n')
    plt.ylabel('Time')
    plt.plot(elements, times, label='Actual Time')
    plt.grid()
    plt.legend()
    plt.show()
    pass

printChart()