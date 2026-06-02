#This problem asks us to find the number under one million whose 
#collatz sequence is longest.

def main():
    print("The purpose of this program is to find the number under a given bound")
    print("with longest Collatz sequence.")

    upperBound = int(input("Please input your desired upper bound."))

    currentMax = 0
    currentMaxLength = 0

    collatzLengthArray = [0,1,2]

    #We save time in calculation by realizing that if at any stage we divide by
    #2 and get a number which we already know the length of a collatz series
    #for then we can just add however many steps it took to get there to find
    #the length for our current number.
    for i in range(3, upperBound):
        steps = 0
        collatzLengthArray.append(1)
        collatz = i
        while(collatz >= 1):
            if(collatz%2 == 0):
                collatz = collatz // 2
                steps = steps + 1
                if len(collatzLengthArray) > collatz:
                    collatzLengthArray[i] = collatzLengthArray[collatz] + steps
                    break
            else:
                collatz = 3*collatz + 1
                steps = steps + 1
        

        if collatzLengthArray[i] > currentMaxLength:
            currentMax = i
            currentMaxLength = collatzLengthArray[i]

    print("The largest collatz chain belongs to", currentMax, ". It has a length of", currentMaxLength)

    return 0

if __name__ == "__main__":
    main()