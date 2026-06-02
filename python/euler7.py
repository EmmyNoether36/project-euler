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

def main():
    print("The purpose of this program is to compute the first n")
    print("prime numbers where n is a natural number.")

    n = int(input("Please enter a natural number n"))

    #We need to know how big of an upper bound to find primes up to.
    #An upper bound is given by nlog(nlog(n)) as long as n is at least 6.

    if n < 6:
        bound = 14
    else:
        bound = math.ceil(n*math.log(n*math.log(n)))

    primesList = sieve(bound)
    print("The nth prime is ", primesList[n-1])
    return 0

if __name__ == "__main__":
    main()