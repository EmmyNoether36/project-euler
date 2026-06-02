import inspect

#This problem asks us to find the maximum sum of a path down a pyramid.
#We can do it by brute force because the pyramid isn't that big.

#We are told that a later problem is similar but features
#a much bigger pyramid. So I'll put off finding a clever
#solution till then.

#We need a good way to organize routes through the pyramid.
#If we organize each row of the pyramid into the arrays a route
# is basically a choice to go down to the next row to the number
#with the same index, or to go to the one with one higher of an index.
#Thus a route corresponds to a binary strings of length 15.


def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               greatest sum achieved by moving down a pyramid
                               of numbers."""))

    pyramid =[[75],\
                [95, 64],\
                [17, 47, 82],\
                [18, 35, 87, 10],\
                [20, 4, 82, 47, 65],\
                [19, 1, 23, 75, 3, 34],\
                [88, 2, 77, 73, 7, 63, 67],\
                [99, 65, 4, 28, 6, 16, 70, 92],\
                [41, 41, 26, 56, 83, 40, 80, 70, 33],\
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],\
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],\
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],\
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],\
                [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],\
                [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
    
    print(pyramid)

    routes = ["0", "1"] 

    while(len(routes) < 2**14):
        currentLength = len(routes)
        for i in range(currentLength):
            routes.append(routes[i] + "0")
            routes.append(routes[i] + "1")
        
        routes = routes[currentLength:]

    maxSum = 0

    for route in routes:
        x = 0
        y = 0
        routeSum = pyramid[x][y]
        for i in range(14):
            y += 1
            x += int(route[i])
            routeSum += pyramid[y][x]
        if routeSum > maxSum:
            maxSum=routeSum

    print("The maximum sum is", maxSum)

    return 0

if __name__ == "__main__":
    main()