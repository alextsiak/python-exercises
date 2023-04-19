'''
EXERCISE DESCRIPTION:

Calculate the probability of two students in a class having the same birthday.
'''
import random

students = input("Enter number of students: ")

def has_duplicates(t):
    total = []
    for elem in t:
        if elem in total:
            return True
        total.append(elem)
    return False

counter = 0

for x in range(1000):
    birthdays = []
    for i in range(int(students)): #generates 23 random birthdays once
        bday = random.randint(1, 365)
        birthdays.append(bday)
    if has_duplicates(birthdays):
        counter += 1


print(f"If there are {students} students in your class, the chance that two of them will have the same birthday is {counter/10}%")
