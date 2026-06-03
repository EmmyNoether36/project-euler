import inspect
from algorithms import sieve
from algorithms import isPrimeList

def circPermute(n: int):
    originalString = str(n)
    permutedString = originalString[len(originalString)-1]
    for digit in originalString[0:len(originalString)-1]:
        permutedString += digit
    return int(permutedString)

def circPermuteList(n: int):
    permuteList = [n]
    for i in range(len(str(n))-1):
        permuteList.append(circPermute(permuteList[i]))
    return permuteList

def main():
    print(inspect.cleandoc("""The purpose of this program is to find how many
                           circular primes there are below one million. A
                           circular prime is one which, if you circularly 
                           permute their digits they are still prime.
                               """))
    
    primesList = sieve(1000000)
    isPrime = isPrimeList(1000000)
    winningNumbers = []

    for p in primesList:
        if p in winningNumbers:
            continue
        permuteList = circPermuteList(p)
        allPrimes = True
        for n in permuteList:
            if not isPrime[n]:
                allPrimes = False
                break
        if allPrimes:
            winningNumbers += permuteList

    winningNumbersSet = set(winningNumbers)

    print("The number of circular primes is", len(winningNumbersSet))


    return 0

if __name__ == "__main__":
    main()