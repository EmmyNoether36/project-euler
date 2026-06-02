def triangle(n):
    return n*(n+1)//2

def sumOfSquares(n):
    return n*(n+1)*(2*n+1)//6

def main():
    print("The purpose of this program is to compute the difference")
    print("between the square of the sum of the first n natural numbers")
    print("and the sum of squares of the first n natural numbers.")

    n = int(input("Please enter a number n."))
    result = triangle(n)*triangle(n) - sumOfSquares(n)

    print("The difference between the sum of squares of the first ", n)
    print("numbers and the square of the sume of the first ", n)
    print("numbers is ", result)

    return 0

if __name__ == "__main__":
    main()