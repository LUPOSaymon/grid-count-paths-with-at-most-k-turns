# Create an array where the array[index] contains the factorial of index-1
def createFactorialArray(z):#O(n)
    factorials = [1] * (z) #(z+1 cause we include
    for i in range(1, z):
        factorials[i] = factorials[i - 1] * (i+1)
    return factorials

def countPaths(n,k):
    return None
# With a grid n*n, count all possible paths with at least k turns
def printPaths(n, k):
    factorials = createFactorialArray(n - 2)
    count = countPaths(n,k)
    print(factorials)


