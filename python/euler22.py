#This problem asks us to sort a list of names alphabetically
#then compute a "name score" for each of them and sum up those
#scores. My way of doing this involves a sorted list.
#You need a custom package to use this, called sortedcontainers.

import inspect
import string
from sortedcontainers import SortedList # type: ignore

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               \"name score\" of various names according to 
                               certain rules and then add up the scores.                             
                               """))
    
    with open("names.txt", "r") as namestream:
        for line in namestream:
            nameList = SortedList(line[1:len(line)-1].split("\",\""))

    scoreList = []

    for i in range(len(nameList)):
        alphValue = 0
        for letter in nameList[i]:
            alphValue += string.ascii_uppercase.index(letter) + 1
        nameScore = (i+1)*alphValue
        scoreList.append(nameScore)

    result = 0

    for score in scoreList:
        result += score

    print("The name score total is", result)

    return 0

if __name__ == "__main__":
    main()