import math

def triangle(n):
    return n*(n+1)//2

#A function which uses the sieve of Erathosthenes to produce a list
#of all prime numbers up to a given bound.
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

def numberOfFactors(num):
    factors = factorize(num)
    numPrimeFactors = len(factors)
    numFactors = 1

    for i in range(numPrimeFactors):
        numFactors = numFactors * (factors[i][1] + 1)
    return numFactors

#Project Euler problem 12 asks us to find the first triangular number with
#over 500 divisors. Note that every tringular number is of the form
#n(n+1)/2. This means that we can find the number of factors of them
#by finding the number of factors of n/2, and n+1 (or reverse them if n+1 is even), 
#and multiplying them (n and n+1 are relatively prime). 

def main():
    print("The purpose of this program is to find the first triangular")
    print("number with at least a given number of factors.")
    n = int(input("Please enter the desired number of factors"))

    numFactors = 0
    m = 1

    while(numFactors <= n):
        if m % 2 == 0:
            numFactors = numberOfFactors(m//2) * numberOfFactors(m+1)
        else:
            numFactors = numberOfFactors(m) * numberOfFactors((m+1)//2)
        m = m + 1
    print("The first triangular number with over", n, "factors is", triangle(m-1))
    return 0

    

if __name__ == "__main__":
    main()