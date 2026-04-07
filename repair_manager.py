"""
ASSIGNMENT 11B: SPRINT 4 - WRITING TO FILES
Project: Repair Manager (V4.0)
Developer: Nick Smoot
"""

import datetime

# --- GLOBAL CONSTANTS ---
PRICES_FILE = "repair_prices.txt"
HISTORY_FILE = "repair_history.txt"

def get_customer_info():
    """Asks for customer's name, phone number/email, and device type"""
    name = input("Customer Name: ").title()
    email = input("Customer Email: ")
    device = input("Device Type: ")
    return name, email, device

def load_prices():
    """Gets repair prices from repair_prices.txt"""
    # TODO: Open and read prices from repair_prices.txt.
    return {}

def calculate_total(device, prices):
    """Calculates the total price for the repair job."""
    # TODO: Calculate price using device and service.
    return 0.0

def create_ticket(customer, price):
    """Builds a new repair job record and saves it to repair_history.txt"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a") as file:
        file.write(f"[{timestamp}]\n")
        file.write(f"Customer: {customer}\n")
        file.write(f"Total: ${price:.2f}\n")
        file.write("-" * 50 + "\n")
    print("Ticket Saved.")

def update_ticket():
    """Finds a job by using its ID and updates its status"""
    # TODO: Search repair_history.txt for a job and update its status.
    pass

def generate_receipt(customer, total):
    """Prints a receipt for the customer"""
    print("\n--- RECEIPT ---")
    print(f"Customer: {customer}")
    print(f"Total: ${total:.2f}")
    print("Thank you!")

def main():
    while True:
        action = input("Enter 'new' to make a new ticket or 'quit' to exit: ").lower().strip()

        if action == 'quit':
            print("Closing Repair Manager.")
            break

        elif action == 'new':

            # 1. Identity Phase
            name, email, device = get_customer_info()
            print(f"Customer: {name} | Email: {email} | Device: {device}")

            # 2. Load Prices Phase
            current_prices = load_prices()

            # 3. Calculation Phase
            total = calculate_total(device, current_prices)

            # 4. Create Ticket Phase
            create_ticket(customer=(name, email, device), price=total)

            # 5. Update Ticket Phase
            update_ticket()

            # 6. Generate Receipt Phase
            generate_receipt(customer=name, total=total)

main()
