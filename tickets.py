"""
ADD-100: Assignment 6A - Ticket Sales
Author: Nick Smoot
Date: 2/23/2026
File: tickets.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# --- 1. Make a list of 20 seats ---

seats = list(range(1, 21))

# --- 2. Ask  for a seat number ---

while True:
    print("Available seats:", seats)
    seat_choice = input("Enter a seat number to book (0 to quit): ")

    # --- 3. Do not allow invalid inputs ---

    if not seat_choice.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    seat_choice = int(seat_choice)

    if seat_choice == 0:
        print("Exiting booking system.")
        break
    elif seat_choice not in seats:
        print("Seat not available. Please choose another seat.")
    else:

        # --- 4. Remove the seat from the list ---

        seats.remove(seat_choice)
        print(f"Seat {seat_choice} booked successfully.")

    # --- 5. Repeat ---

    if not seats:
        print("All seats are booked. Exiting booking system.")
        break