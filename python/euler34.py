import inspect

fact = [1,1,2,6,24,120,720,5040,40320,362880]

def factorialSum(n):
    sum = 0
    for digit in str(n):
        sum += fact[int(digit)]
    return sum

def main():
    print(inspect.cleandoc("""The purpose of this program is to find the sum
                           of all numbers which are equal to the sum of the
                           factorial of their digits. Note, 1 and 2 are not counted.                              
                               """))

    #Note that
    #  0! = 1
    #  1! = 1
    #  2! = 2
    #  3! = 6
    #  4! = 24
    #  5! = 120
    #  6! = 720
    #  7! = 5040
    #  8! = 40320
    #  9! = 362880
    #My first impression is that in order for smaller numbers
    #to satisfy our conditions, they must have small digits.
    #For instance, no number under 362880 can have a 9 in it
    #if it satisfies our conditions. Similarly an n digit
    #number can have factorial sum at most n*362880 so there
    #will be an upper limit. I'm not sure how big, so I'll make
    #some guesses.

    winningNumbers = []
    for i in range(3, 10000000):
        if factorialSum(i) == i:
            winningNumbers.append(i)

    result = sum(winningNumbers)

    print("The sum is", result)

    return 0

if __name__ == "__main__":
    main()