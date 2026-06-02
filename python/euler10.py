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

def main() :
    print("The purpose of ths program is to fnd the sum of all")
    print("primes below some upper bound.")
    n = int(input("Please enter an upper bound."))

    primeList = sieve(n)
    result = sum(primeList)
    print("The sum is ", result)
    return 0

if __name__ == "__main__":
    main()