"""
ADD-100: Assignment 11A - The Bug Tracking Log
Author: Nick Smoot
Date: 4/6/2026
File: bug_tracker.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[x] 1. Program uses a while loop to keep asking for bugs.
[x] 2. Uses the datetime module to get a timestamp format.
[x] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[x] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[x] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

# --- 1. Loop ---
while True:
    action = input("Enter 'log' to record a bug, or 'quit' to stop: ").lower().strip()

    if action == "quit":
        print("Bug log updated.")
        break

    elif action == "log": 

# --- 2. Ask User For Input ---

        file_name = input("File name:" )
        description = input("Description of the error: ")
        priority = input("Priority (High, Medium, Low): ")

# --- 3. Timestamp and Dictionary ---

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        bug = {timestamp: [file_name, description, priority]}

# --- 4. Write to File ---
        with open("bug_log.txt", "a") as file:
            file.write(f"[{timestamp}]\n")
            file.write(f"File: {file_name}\n")
            file.write(f"Status: {description}\n")
            file.write(f"Priority: {priority}\n")
            file.write("-" * 50 + "\n")

        print("Bug Logged")
