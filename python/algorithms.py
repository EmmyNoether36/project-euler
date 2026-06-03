import math

def triangle(n):
    return n*(n+1)//2

def sumOfSquares(n):
    return n*(n+1)*(2*n+1)//6

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

def isPrimeList(n):
    if(n < 0):
        n = -n
    if(n <= 1):
        return False
    
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    prime = 2
    while prime <= n:
        current = 2*prime
        while(current <= n):
            isPrime[current] = False
            current = current + prime
        prime = prime + 1
        while prime < n and not isPrime[prime]:
            prime = prime + 1
    return isPrime

def isPrime(n):
    if(n < 0):
        n = -n
    if(n <= 1):
        return False
    
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    prime = 2
    while prime <= n:
        current = 2*prime
        while(current <= n):
            isPrime[current] = False
            current = current + prime
        prime = prime + 1
        while prime < n and not isPrime[prime]:
            prime = prime + 1
    return isPrime[n]

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

def gcd(n, m):
    if n < 0:
        n = -n
    if m < 0:
        m = -m
    if n < m:
        temp = m
        m = n
        n = temp
    if m == 0:
        return n

    r0 = n
    r1 = m
    r2 = r0 % r1

    while r2 > 0:
        r0 = r1
        r1 = r2
        r2 = r0 % r1

    return r1

def lcm(n, m):
    return abs(n*m//gcd(n,m))

def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact