
def triangle(n):
    return n*(n+1)//2

def main():
    print("This is a program for computing the sum of all numbers which are")
    print("multiples of n or multiples of m. Here n and m are natural numbers")
    print("We will compute the sum over all numbers up to an upper bound.")
    n = int(input("Enter n. This must be a natural number."))
    m = int(input("Enter m. This must be a natural number."))
    bound = int(input("Enter the upper bound."))
    sum = n*(triangle(int(bound/n))) + m*(triangle(int(bound/m))) - n*m*(triangle(int(bound/(n*m))))
    print("The sum is: ", sum)
    return 0

if __name__ == "__main__":
    main()