"""
WORK IN PROGRESS    
say.py - Given a number from 0 to 999,999,999,999, spells out that number in English.
"""
basics = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def say(number):
    if number < 0:
        raise ValueError("Input out of range!")
    elif number < 20:
        return basics[number]
    elif number in tens.keys():
        return tens[number]
    elif number < 100:
        return f"{say(number-number%10)}-{say(number%10)}"
    else:
        raise ValueError("Input out of range!")

print(say(95))