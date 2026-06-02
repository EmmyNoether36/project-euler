#I'm doing this completely directly because I think
#it'll be fast enough. We could also have done some
#analysis and probably have solved this with a straight
#arithmetic calculation.

import inspect

def main():
    print(inspect.cleandoc("""The purpose of this program is to compute the
                               number of Sundays that fell on the first of
                               the month during the 20th century
                               (1 Jan 1901 to 31 Dec 2000)"""))

    #We have an array of the number of days of each month
    #Actually, we save their least residue mod 7 because 
    #adding that will have the same effect on the day of
    #the week as adding the actual number
    #28 % 7 = 0, 30 % 7 = 2, 31 % 7 = 3
    numDays = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    
    currentMonth = 0
    currentWeekDay = 1
    currentYear = 1900
    count = 0

    while(currentYear < 2001):
        if currentWeekDay == 0:
            count += 1
        isLeapYear = (currentYear % 400 == 0) or ((currentYear % 4 == 0) and not (currentYear % 100 == 0))
        currentWeekDay = (currentWeekDay + numDays[currentMonth]) %7
        if (currentMonth == 1) and isLeapYear:
            currentWeekDay = (currentWeekDay + 1) % 7
        currentMonth = (currentMonth + 1) % 12
        if currentMonth == 0:
            currentYear += 1

    #This overcounts because we were supposed to start in 1901
    #There were two Sundays at the start of the month in 1900.

    count -= 2

    print("The number of Sundays that fell on the first of")
    print("the month in the twentieth century is", count)
    
    return 0

if __name__ == "__main__":
    main()