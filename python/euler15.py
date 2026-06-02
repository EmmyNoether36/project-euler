#This problem asks us, in a 20 by 20 grid, how many routes
#are there from the top left to the bottom right where
#we always either move right or down.

#Note that when we are at the top we can move right
#any amount from 0 to 20. At the next level we can move
#right any amount less than or equal to 20 - n where
#n is the amount we moved in the first step.

#The process #continues like this, and in the end
#the numbers must add up to 20.
#So the answer should be the number
#of sequences of 20 numbers between 0 and 20
#which add to 20.

#In other words we almost want he number of
#compositions of 20. The only difference is
#we need to add 0s somewhere if we have less than
#20 positive summands.

#One way to find this number would be to use a recursive
#algorithm building our sums from smaller sums.

#However, we can also just use combinatorics to solve this.
#In any correct route there will be 10 moves to the right
#and 10 moves down. We're just choosing an order for them.
#To make it even simpler we really only need to choose
#10 of them to be down moves as the rest will all be right.

def main():
    print("The purpose of this program is to figure out how")
    print("many routes there are from the top left corner")
    print("to the bottom right corner of an n by n grid")

    n = int(input("Enter the size of the grid."))

    num = 1
    den = 1

    for i in range(1,n+1):
        num = num*(n+i)
        den = den*i
    
    routes = num//den



    print("There are", routes, "routes.")

    return 0

if __name__ == "__main__":
    main()