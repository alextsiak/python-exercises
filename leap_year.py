def leap():
    '''Returns True if the given year is a leap year'''
    year = int(input("Please enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        return True
    else:
        return False

