import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to count how
                               many letters it takes to write out the first
                               1000 numbers."""))

    numberWords = {0:"",
                   1:"one",
                   2:"two",
                   3:"three",
                   4:"four",
                   5:"five",
                   6:"six",
                   7:"seven",
                   8:"eight",
                   9:"nine",
                   10:"ten",
                   11:"eleven",
                   12:"twelve",
                   13:"thirteen",
                   14:"fourteen",
                   15:"fifteen",
                   16:"sixteen",
                   17:"seventeen",
                   18:"eighteen",
                   19:"nineteen",
                   20:"twenty",
                   30:"thirty",
                   40:"forty",
                   50:"fifty",
                   60:"sixty",
                   70:"seventy",
                   80:"eighty",
                   90:"ninety",
                   1000:"onethousand"}
    
    for i in range(11, 1000):
        if(not i in numberWords.keys()):
            if(i<100):
                numberWords[i] = numberWords[i - i%10] + numberWords[i%10]
            else:
                numberWords[i] = numberWords[i//100] + "hundred"
                if(i%100!=0):
                    numberWords[i] = numberWords[i] + "and" + numberWords[i%100]


    sum = 0
    for i in numberWords.values():
        sum = sum + len(i)

    print("The total is", sum)
    return 0

if __name__ == "__main__":
    main()