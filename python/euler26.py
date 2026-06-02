#This problem asks us to find the value of d < 1000 for which 1/d
#contains the longest recurring cycle in its decimal fraction part.

#This one feels like it takes some thought. Just dividing, using a
#float would likely not be accurate enough.

#wWe get the decimal expansion by repeatedly
#multiplying a number by 10 and dividing by the
#denominator, so what we're looking for is the
#multiplicative order of 10 mod m.

#A little thinking reveals that the numbers 2 and 5,
#being the only primes that go into 10, aren't important.
#If n=2^x5^ym where m is relatively prime with 2 and 5
#then its period is only determined by m.



import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               find  the value of d < 1000 for which 1/d
                                contains the longest recurring cycle in its
                                decimal fraction part.
                               """))

    periodList = [0,1,1]

    maxLength = 1
    maxNum = 2

    for den in range(3, 1000):
        newden = den
        while(newden % 2 == 0):
            newden = newden//2
        while(newden % 5 == 0):
            newden = newden//5

        if newden == 1:
            periodList.append(0)
            continue

        currentPower = 1
        currentNum = 10 % newden

        while(currentNum != 1):
            currentPower += 1
            currentNum = (currentNum * 10) % newden

        periodList.append(currentPower)


    maxLength = max(periodList)
    maxNum = periodList.index(maxLength)

    print("The numer with longest cycle length is", maxNum, "with cycle length", maxLength)

    return 0

if __name__ == "__main__":
    main()