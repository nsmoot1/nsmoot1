"""
ADD-100: Assignment 5A - Input Validation 
Author: Nick Smoot
Date: 2/16/2026
File: registration.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# --- 1. Name ---

first_name = input("Enter your first name: ")

while first_name == "":
    print("First name cannot be blank.")
    first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

while last_name == "":
    print("Last name cannot be blank.")
    last_name = input("Enter your last name: ")

# --- 2. Phone Number ---

phone_number = input("Enter your phone number: ")

while phone_number == "":
    print("Phone number cannot be blank.")
    phone_number = input("Enter your phone number: ")

# --- 3. Chaperone (Y/N) ---

chaperone = input("Do you have a chaperone? (Y/N): ").upper()

while chaperone != "Y" and chaperone != "N":
    print("Please enter Y or N only.")
    chaperone = input("Do you have a chaperone? (Y/N): ").upper()

# --- 4. Ticket Count ---

ticket_count = input("How many tickets do you want? ")

while not ticket_count.isdigit() or int(ticket_count) <= 0:
    print("Ticket count must be a number greater than 0.")
    ticket_count = input("How many tickets do you want? ")

ticket_count = int(ticket_count)

# --- 5. Output ---

print("\nRegistration Complete.")
print("Name:", first_name, last_name)
print("Phone:", phone_number)
print("Tickets:", ticket_count)

if chaperone == "Y":
    print("Chaperone: Yes")
else:
    print("Chaperone: No")
