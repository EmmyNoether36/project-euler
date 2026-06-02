#This problem asks us to consider quadratics of the form
#n^2 + an + b where |a| < 1000 and |b| <= 1000, and find
#the quadratic which produces the most primes for
#consecutive values of n starting with n = 0.

#Initial observations:
#Any such quadratic will produce at most b-1 primes.
#This is because b^2 + b + b is definitely divisible
#by b. Further if b = cd, d^2 + d + cd is divisible
#by d, so if b is composite the expression can only
#produce primes up to its smallest positive prime
#factor.

#I initially just tried to brute force this but the
#numbers involved are large enough this seemed to take
#too long.

#This was probably because I wasn't saving the list of
#primes in my list so I was repeatedly recalculating.
#I fixed this by making an educated guess how big a list
#of primes I needed and made the list once.

import inspect
import math

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

def quadratic(a,b,n):
    return n*n+a*n+b


def main():
    print(inspect.cleandoc("""Consider quadratics of the form n^2 + an + b
                           where |a| < 1000 and |b| <= 1000. The purpose of
                           this program is to determine the product of a and
                           b for the quadratic which produces the maximum
                           number of primes for consecutive values of n,
                           starting with n=0.
                               """))

    maxPrimes = 0

    #I need a list of the prime status of all numbers
    #that might come up as outputs of my quadratics.
    #To figure out how much I need, note that
    #|n^2 + an + b| <= n^2 + |a|n + |b|
    #In our case this is bounded by n^2 + 999n + 1000
    #We know that n has to be smaller than b to output
    #primes so an upper bound is
    #1000^2 + 999*1000 + 1000

    isPrime = isPrimeList(1000*1000 + 999*1000 + 1000)

    for a in range(-999, 999):
        for b in range(-1000, 1000):
            n = 0
            while(isPrime[abs(quadratic(a,b,n))]):
                n += 1
            if n > maxPrimes:
                maxPrimes = n
                maxa = a
                maxb = b
    
    print("The product in question is", maxa*maxb)

    return 0

if __name__ == "__main__":
    main()