"""
ADD-100: Assignment 12A - The Configurable Menu & Auditor
Author: Nick Smoot
Date: 4/13/2026
File: menu_reader.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. PHASE 1: External menu_config.txt file created in workspace.
[x] 3. Program reads and parses the .txt file into a Dictionary.
[x] 4. PHASE 2: break the dictionary into individual variables.
[x] 6. Print each category and its details
[x] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

# 1. --- Reads and parses menu_config.txt ---

def read_menu():
    menus = {}
    try:
        with open ("menu_config.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split("  :")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail 
        return menus
    except FileNotFoundError:
        print ("Menu file not found. Please run menu_creator.py.")

# 2. --- Breaks into individual category variables ---

def split_into_variables(menu_items):
    entrees = menu_items.get("ENTREES")
    sides = menu_items.get("SIDES")
    drinks = menu_items.get("DRINKS")
    deserts = menu_items.get("DESSERTS")
    return entrees, sides, drinks, deserts

# 3. --- Prints menu category and items ---
        
def print_menu(entrees, sides, drinks, deserts):
    print("\n--- Nicks Menu ---")
    print(f"Entrees: {entrees}")
    print(f"Sides: {sides}")
    print(f"Drinks: {drinks}")
    print(f"Deserts: {deserts}")

def main():
    menu_items = read_menu()
    if menu_items is None:
        return
    entrees, sides, drinks, deserts = split_into_variables(menu_items)
    print_menu(entrees, sides, drinks, deserts)

main()