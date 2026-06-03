import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to find the
                               numbers which can be written as the sum of
                                the fifth powers of their digits.
                               We will then take the sum of these.
                               """))

    winningNumbers = []

    for n in range(2,999999):
        digitSum = 0
        for digit in str(n):
            digitSum += int(digit)**5
        if n == digitSum:
            winningNumbers.append(n)

    finalSum = sum(winningNumbers)

    print("The sum is", finalSum)

    return 0

if __name__ == "__main__":
    main()