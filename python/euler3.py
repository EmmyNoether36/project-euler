import math

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
        

def main():
    print("This is a program for finding the largest prime factor of a given number.")
    n = int(input("Please enter the number you want the largest prime factor of.\n"))

    factors = factorize(n)

    print("The prime factorization of ", n, " is ", factors)

    return 0


if __name__ == "__main__":
    main()