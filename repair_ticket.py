"""
ASSIGNMENT 13B: SPRINT 6 - REPAIR TICKET CLASS
Project: Repair Manager
Developer: Nick Smoot
"""

class RepairTicket:
    def __init__(self, name, email, device):
        self.__name = name
        self.__email = email
        self.__device = device
        self.__service = ""
        self.__price = 0.0
        self.__status = "Received"

    # 1. --- Getters ---
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_device(self):
        return self.__device

    def get_service(self):
        return self.__service

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    # 2. --- Setters ---
    def set_service(self, service):
        self.__service = service

    def set_price(self, price):
        self.__price = price

    def set_status(self, status):
        self.__status = status

    # 3. --- Display ---
    def display_ticket(self):
        print("\n--- Repair Ticket ---")
        print(f"1) Customer Name: {self.__name}")
        print(f"2) Email: {self.__email}")
        print(f"3) Device: {self.__device}")
        print(f"4) Service: {self.__service}")
        print(f"5) Price: ${self.__price:.2f}")
        print(f"6) Status: {self.__status}")

    # 4. --- Test Objects ---
ticket1 = RepairTicket("Nick Smoot", "Nick@gmail.com", "Laptop")
ticket1.set_service("Diagnostics")
ticket1.set_price(40.00)
ticket1.display_ticket()

ticket2 = RepairTicket("Computer Man", "ComputerMan@gmail.com", "Desktop")
ticket2.set_service("Virus Removal")
ticket2.set_price(90.00)
ticket2.display_ticket()