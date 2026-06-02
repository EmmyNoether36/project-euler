#This problem asks us to find the sum of all amicable numbers
#under 10000. Amicable numbers of pairs of numbers
#a and b, where d(a) = b and d(b) = a. Here d is the sum of
#proper divisors function.

#This should be straightforward. d is a multiplictive function
#meaning it can be calculated for an arbitrary n by finding the
#prime factorization of n, applying it to the prime powers in that
#factorization and then multiplying the result.

#Note that I'm using d to be the sum of all divisors,
#not just proper divisors. This is easier to calculate
#and note that if a and b are amicable then using my
#function d, d(a) = d(b), and the converse as well.

import math
import inspect

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



def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               sum of all amicable numbers under 10000.                               
                               """))
    
    knownAmicables = {220:284}

    for a in range(2,10000):
        if(a in knownAmicables.values()):
            continue
        b = d(a) - a
        if(a == b):
            continue
        if  d(b) == d(a):
            knownAmicables[a] = b

    print(knownAmicables)

    result = 0

    for a in knownAmicables.keys():
        result += a + knownAmicables[a]

    print("The sum of all amicable pairs below 10000 is", result)

    return 0

if __name__ == "__main__":
    main()