#This problem asks us to take the permutations of a
#digits 0 through 9, and identify which one is millionth
#in legicographic order.

#Thinking about this a little bit reveals that there are
#9! = 362880 permutations beginning with 0, followed by
#another 362880 permutations beginning with 1. The millionth
#one should therefore begin with 2.  We can begin our search
#there, at the 725760th permutation.

#Following the same reasoning, of the permutations beginning
#with 2, there are 8!=40320 with a 0 as their second digit.
#40320 with a 1 as their second digit, et cetera.

#This reasoning tells us the correct permutation begins with 27

#Next up, there are 7!=5040 that begin with 270, etc.
#We use this to determine it begins with 278.

#Our program is just going to work though these possibilities.

import inspect

def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                              which permutation is the millionth in
                              legicographic order.                               
                               """))
    
    currentPerms = 0
    desiredPerm = 1000000
    availableDigits = [0,1,2,3,4,5,6,7,8,9]
    correctPerm = []
    step = 9


    #There are 10! total permutations. The first 9! begin with 0.
    #The second 9! begin with 1, etc.

    while step >= 0:
        i = 0
        while(currentPerms + factorial(step) < desiredPerm):
            i += 1
            currentPerms += factorial(step)
        correctPerm.append(availableDigits.pop(i))
        step -= 1


    print("The correct permutation is", correctPerm)

    return 0

if __name__ == "__main__":
    main()