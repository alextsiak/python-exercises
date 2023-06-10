"""
WORK IN PROGRESS
say.py - Given a number from 0 to 999,999,999,999, spells out that number in English.
"""
basics = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}

decs = {"20": "twenty", "30": "thirty", "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy", "80": "eighty", "90": "ninety"}

def say():
    number = input("Please enter a number: ")

    #basic cases: 0-99
    if len(number) == 1:
        print(basics[number])
    elif len(number) == 2:
        if number in basics.keys():
            print(basics[number])
        if number in decs.keys():
            print(decs[number])
    else:
        raise ValueError("Input out of range!")

say()