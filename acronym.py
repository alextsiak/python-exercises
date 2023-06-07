'''
acronym.py - Converts a phrase to its acronym.
'''

phrase = input("Please enter a phrase: ")
acronym = ''

for word in phrase.split('-'):
    for w in word.split():
        acronym += w[0]

print(acronym)