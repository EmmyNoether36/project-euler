def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# A little analysis will show that every third fibonacci number
# is even. (The pattern will be odd odd even because addibg
# an even to an even yields an odd but adding two odds
# gives an even). After this, a little algebra gives
# a recursion relation for even fibonaccis.
def evenFibonacci(n):
    if n == 1:
        return 2
    if n==2:
        return 8
    else:
        return evenFibonacci(n-2) + 4*evenFibonacci(n-1)

def main():
    print("This is a program for computing the sum of")
    print("even fibonacci numbers smaller than an upper bound.")
    bound = int(input("Input the upper bound."))
    sum = 0
    i = 2
    currentFib = evenFibonacci(1)
    while(currentFib < bound):
        sum = sum + currentFib
        currentFib = evenFibonacci(i)
        i = i + 1
    print("The sum of even fibonacci numbers less than ", bound, "is ", sum)
    return 0

if __name__ == "__main__":
    main()