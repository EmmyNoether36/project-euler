#For this problem we have to compute the digit sum of 100!
#I'm brute forcing this because I think I can.

import inspect

def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                              sum of the digits of 100!"""))

    bigNumStr = str(factorial(100))

    sum = 0

    for digit in bigNumStr:
        sum += int(digit)

    print("The sum of digits of 100! is", sum)

    return 0

if __name__ == "__main__":
    main()