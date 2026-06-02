def main():
    print("The purpose of this program is to find the largest")
    print("palindrome which is the product of two three digit numbers")

    current1 = 999
    current2 = 999
    currentbest = 0
    
    while current1 > 100:
        currentprod = current1*current2
        currentstring = str(currentprod)
        if currentstring == currentstring[::-1]:
            if currentprod > currentbest:
                currentbest = currentprod
        if current2 == 100:
            current2 = current1 - 1
            current1 = current1 - 1
        else:
            current2 = current2 - 1
    print("The largest palindrome which is the product of two")
    print("three digit numbers is ", currentbest)
    return 0

if __name__ == "__main__":
    main()