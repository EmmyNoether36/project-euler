import math

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

#It is well-known since the time of Euclid that one can generate primitive
#Pythagorean triples by picking two integers m and n such that m and n are 
#coprime and exactly one of the two is even, m > n > 0, and using the formulas
#a = m^2-n^2
#b = 2mn
#c = m^2 + n^2
#We can then get the nonprimitive triples by multiplying primitive triples
#by integers.
def primPythTriple(m,n):
    if(m < n):
        temp = m
        m = n
        n = temp
    triple = [m**2 - n**2, 2*m*n, m**2 + n**2]
    return triple

#Note that this means the sume of a primitive Pythagorean triple in this form is
#m^2 - n^2 + 2mn + m^2 + n^2 = 2(m^2 + mn)
#and then a nonprimitive triple given by a times one of these has sum
#2a(m^2 + mn)
#This in particular tells us that the sum is always even and that increasing n
#increases the sum by multiples of 2am. Thus we can run three nested loops, iterating m
#on the outside and iterating n on the inside, and then iterating a on the
#innermost loop until we get to 1000.

def main():
    print("The purpose of this program is to find the unique Pythagorean")
    print("triple (a, b, c) such that a + b + c = 1000.")
    print("A Pythagorean triple is a triple of integers (a,b,c)")
    print("such that a^2 + b^2 = c^2.")

    m = 2

    correctTriples = []

    triple = [1,1,1]
    while m < math.ceil(math.sqrt(1000)):
        n = 1
        while n < m:
            if gcd(m,n) == 1:
                triple = primPythTriple(m,n)
            else:
                n += 2
                continue
            a = 1
            while sum([i * a for i in triple]) <= 1000:
                if sum([i * a for i in triple]) == 1000:
                    correctTriples.append([i * a for i in triple])
                a += 1
            n += 2
        m += 2
    
    print("The correct triples are")
    print(correctTriples)


    return 0

if __name__ == "__main__":
    main()