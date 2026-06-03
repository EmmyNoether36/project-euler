import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               number of ways there are to make 2 British pounds.
                               """))

    # 2 pounds are 200 pence. We just need to set
    #up some variables with various coin and bill
    #values and find all the ways they add up to 200

    winningNumbers = [(0,0,0,0,0,0,0,1)]

    for g in range(3):
        for f in range(5-2*g):
            for e in range(11 - 5*g - 2*f):
                for d in range(21 - 10*g - 5*f - 2*e):
                    for c in range(41 - 20*g - 10*f - 4*e - 2*d):
                        for b in range(101 - 50*g - 25*f - 10*e - 5*d - 2*c):
                            for a in range(201 - 100*g - 50*f - 20*e - 10*d - 5*c - 2*b):
                                    if(a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g == 200):
                                        winningNumbers.append([a,b,c,d,e,f,g,0])                                


    print("There are", len(winningNumbers), "different ways to make 2 pounds")

    return 0

if __name__ == "__main__":
    main()