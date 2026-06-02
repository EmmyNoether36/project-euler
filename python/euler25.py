#This problems asks us to find the index of the first term
#in the Fibonacci sequence with 1000 digits.

import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               the index of the first Fibonacci number which
                               has 1000 digits.
                               """))

    Flast = 1
    Fcurrent = 1
    Ftemp = 1

    index = 2

    while(len(str(Fcurrent)) < 1000):
        Ftemp = Fcurrent
        Fcurrent += Flast
        Flast = Ftemp
        index += 1

    print("The first Fibonacci number with 1000 digits occurs at the index", index)
    
    return 0

if __name__ == "__main__":
    main()