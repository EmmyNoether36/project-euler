#This problem asks us to consider a spiral formed by
#starting with 1 in the center, moving initially right
#and putting a 2, then moving down, putting a 3, etc.
#until a spiralsize by spiralsize spiral is formed.

#We are then asked to find the sum of the diagonal
#entries.

#I did this a very naive way, by actually constructing the spiral
#It would probably be much faster to just work out the pattern
#on how the new diagonal entries change as the spiral grows
#and calculate this recursively.

import inspect

spiralsize = 1001

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               sum of the diagonal entries of a spiralsize by spiralsize
                               spiral.
                               """))

    #First we initialize the spiral with 0s
    spiral = [[0 for i in range(spiralsize)] for j in range(spiralsize)]

    #Now we want to populate the array.
    x = spiralsize//2
    y = spiralsize//2
    spiral[x][y] = 1
    num = 2

    y += 1
    spiral[x][y] = num
    num += 1

    x += 1
    spiral[x][y] = num
    num += 1

    for j in range(2):
        y -= 1
        spiral[x][y] = num
        num += 1

    for j in range(2):
        x -= 1
        spiral[x][y] = num
        num += 1

    for j in range(2):
        y += 1
        spiral[x][y] = num
        num += 1

    for i in range(3, (spiralsize//2) + 2):
        y += 1
        spiral[x][y] = num
        num += 1

        for j in range(2*(i-2) + 1):
            x += 1
            spiral[x][y] = num
            num += 1

        for j in range(2*(i-2) + 2):
            y -= 1
            spiral[x][y] = num
            num += 1

        for j in range(2*(i-2) + 2):
            x -= 1
            spiral[x][y] = num
            num += 1

        for j in range(2*(i-2) + 2):
            y += 1
            spiral[x][y] = num
            num += 1
        
    sum = 0

    for i in range(spiralsize):
        sum += spiral[i][i]
        sum += spiral[spiralsize - i - 1][i]

    sum -= spiral[spiralsize//2][spiralsize//2]

    print("The product is", sum)

    return 0

if __name__ == "__main__":
    main()