def gcd(n, m):
    if n < 0:
        n = -n
    if m < 0:
        m = -m
    if n < m:
        temp = m
        m = n
        n = temp
    if m == 0:
        return n

    r0 = n
    r1 = m
    r2 = r0 % r1

    while r2 > 0:
        r0 = r1
        r1 = r2
        r2 = r0 % r1

    return r1

def lcm(n, m):
    return abs(n*m//gcd(n,m))

def main():
    print("The purpose of this program is to compute the smallest")
    print("number evenly divisible by all numbers up to a given number.")
    n = int(input("Please enter the number you want to use."))

    index = 3
    current = 2
    while index <= n:
        current = lcm(current, index)
        index = index + 1
        print(index, current)

    print("The smallest number divisible by all numbers up to ", n, " is ", current)
    
    return 0


if __name__ == "__main__":
    main()