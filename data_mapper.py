"""
ADD-100: Assignment 8A - Dictionary Practice - NATO Translator
Author: Nick Smoot
Date: 3/02/2026
File: data_mapper.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[x] 3. Program takes a word and uppercases it.
[x] 4. Program loops through letters and prints NATO words.
[x] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# --- 1. Dictionary --- 

NATO_ALPHABET = {
        "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
        "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
        "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray", "Y":"Yankee","Z":"Zulu"
    }

# --- 2. input ---

word = input("Enter word to spell: ").upper().strip()

# --- 3. Loop and try/except block ---

for letter in word:
    try:
        print(NATO_ALPHABET[letter])
    except KeyError:
        print(f"'{letter}' is not valid.")





