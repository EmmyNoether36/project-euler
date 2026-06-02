#This problem asks us to calculate the sum of the digits of 2^1000.
#One naive approach would be to just calculate 2^1000.
#This is a big number, however, so I expected this to 
#take a while. It really didn't though so I think Python
#has a relatively thoughtful exponentiation algorithm.

def main():
    print("The purpose of this program is to find the sum")
    print("of the digits of the number 2^1000")

    n = 2**1000

    digitString = str(n)

    sum = 0

    for i in range(len(digitString)):
        sum = sum + int(digitString[i])

    print("The sum is", sum)

    return 0

if __name__ == "__main__":
    main()