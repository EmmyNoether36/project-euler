import inspect
import math

#This problem asks us to find the sum of all positive
#integers which cannot be written as the sum of two
#abundant numbers. They note that it is proven all
#numbers greater than 28123 can be written as the sume
#of two abundant numbers.

def sieve(upperBound):
    if(upperBound <= 1):
        return []
    
    isPrime = [True]*upperBound
    isPrime[0] = False
    isPrime[1] = False
    prime = 2
    while prime < upperBound:
        current = 2*prime
        while(current < upperBound):
            isPrime[current] = False
            current = current + prime
        prime = prime + 1
        while prime < upperBound and not isPrime[prime]:
            prime = prime + 1
    primeList = []
    i = 0
    while i < upperBound:
        if isPrime[i]:
            primeList.append(i)
        i = i+1
    return primeList

def factorize(num):
    primeList = sieve(int(math.sqrt(num))+1)
    currentPrimeIndex = 0
    currentNum = num
    factorList = []
    while currentPrimeIndex < len(primeList):
        currentPrime = primeList[currentPrimeIndex]
        exponent = 0
        while currentNum % currentPrime == 0:
            exponent = exponent + 1
            currentNum = currentNum//currentPrime
        if exponent > 0:
            factorList.append([currentPrime, exponent])
        currentPrimeIndex = currentPrimeIndex + 1

    if currentNum > 1:
        factorList.append([currentNum,1])
    return factorList

def d_prime_power(p,e):
    return (p**(e+1)-1)//(p-1)

def d(n):
    factorization = factorize(n)

    divisorSum = 1

    for pair in factorization:
        divisorSum *= d_prime_power(pair[0],pair[1])
    
    return divisorSum

def isAbundant(n):
    return d(n) > 2*n

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                              the sum of all positive integers which cannot
                              be written as the sum of two abundant numbers.
                               """))

    #First we find all abundant numbers up to 28123.
    abundantList = []
    for i in range(2,28124):
        if isAbundant(i):
            abundantList.append(i)
    
    #Now we make a set of all sums of two abundant numbers.
    sumList = []
    for i in range(len(abundantList)):
        for j in range(i, len(abundantList)):
            if(abundantList[i] + abundantList[j] > 28123):
                break
            sumList.append(abundantList[i] + abundantList[j])
    
    sumSet = set(sumList)

    result = 0

    for summand in sumSet:
        result += summand

    result = 28123*28124//2 - result

    print("The sum is", result)

    return 0

if __name__ == "__main__":
    main()