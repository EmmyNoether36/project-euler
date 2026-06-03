import inspect
from eulerTypes import Rational

def main():
    print(inspect.cleandoc("""Note that the number 49/98 can be simplified incorrectly
                           by canceling the 9s to get 4/8, which, coincidentally, is correct.
                           The purpose of this program is to find the four non-trivial examples
                           of this behavior less than one in value and containing two digits in
                           both the numerator and denominator.
                           We will then take the product of these, put it in lowest terms, and 
                           find its denominator.
                               """))

    prod = Rational(1,1)

    for a in range(10, 100):
        for b in range(a+1, 100):
            candidate = Rational(a,b)
            candidateNumString = str(a)
            candidateDenString = str(b)
            for digit in candidateNumString:
                if digit in candidateDenString and digit != "0":
                    candidateNumString = candidateNumString.replace(digit, "")
                    candidateDenString = candidateDenString.replace(digit, "")
                    try:
                        newNum = Rational(candidateNumString + "/" + candidateDenString)
                    except:
                        continue
                    if candidate == newNum:
                        prod *= candidate
                        candidate.print()

    prod = prod.simplify()          
    print("The product in lowest terms is", str(prod))
    return 0

if __name__ == "__main__":
    main()