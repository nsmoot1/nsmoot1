"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[x] 1. Header Docstring included with your name.
[x] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[x] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[x] 4. Task 3: Validation (isdigit check) completed.
[x] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Nick Smoot
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR ---

instrument = "Acoustic Guitar"
print("Length", len(instrument))

print("First letter", instrument[0])
print("Last letter", instrument[-1])

print("Lowest ASCII", min(instrument))
print("Highest ASCII", max(instrument))


# --- TASK 2: THE CLEANUP CREW ---
messy_input = "   vOLUME_knob_11   "

clean_input = messy_input.strip().upper().replace("_", " ")
print("\nCleaned Input:", clean_input)


# --- TASK 3: THE VALIDATOR ---

serial_number = "90210"

if serial_number.isdigit():
    print("Valid Serial")
else: 
    print("Invalid Serial")


# --- TASK 4: THE DUCK BRIDGE ---

name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)
    print("There was a teacher who had a duck and Ducky was his Name-o\n")
    print(f"({current_name}) \n" * 3)
    print("and Ducky was his Name-o!\n")
    duck_letters[count] = "🦆"
    count += 1

" ".join(duck_letters)

