"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Repair Manager (V1.0)
Developer: Nick Smoot
"""

# --- GLOBAL CONSTANTS ---
PRICES_FILE = "repair_prices.txt"
HISTORY_FILE = "repair_history.txt"

def get_customer_info():
    """Asks for customer's name, phone number/email, and device type"""
    # TODO: Ask for name, phone/email, and device.
    return "Nick Smoot", "nicksmoot@gmail.com", "Laptop"

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
    # TODO: Generate job ID, assign status "Received", and save it to file.
    pass

def update_ticket():
    """Finds a job by using its ID and updates its status"""
    # TODO: Search repair_history.txt for a job and update its status.
    pass

def generate_receipt(customer, total):
    """Prints a receipt for the customer"""
    # TODO: Print a formatted receipt for the customer.
    pass

def main():
    # 1. Identity Phase
    name, email, device = get_customer_info()
    print(f"Customer: {name} | Email: {email} | Device: {device}")

    # 2. Load Prices Phase
    current_prices = load_prices()

    # 3. Calculation Phase
    total = calculate_total(device, current_prices)

    # 4. Create Ticket Phase
    create_ticket((name, email, device), total)

    # 5. Update Ticket Phase
    update_ticket()

    # 6. Generate Receipt Phase
    generate_receipt(name, total)

main()