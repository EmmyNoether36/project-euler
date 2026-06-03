#Ths problem asks us how many distinct numbers are of the form
#of the form a^b with 2 <= a, b <= 100

import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute how many
                               distinct numbers are of the form a^b with
                               2 <= a, b <= 100.
                               """))
    
    numberList = []

    for a in range(2, 101):
        for b in range(2, 101):
            numberList.append(a**b)

    numberSet = set(numberList)

    print("There are", len(numberSet), "numbers of this form.")

    return 0

if __name__ == "__main__":
    main()