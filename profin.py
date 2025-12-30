import json
import os 

FILE_NAME = "tickets.json"


# Initialize JSON file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)


# Load tickets from JSON
def load_tickets():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save tickets to JSON
def save_tickets(tickets):
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)


# Generate next ticket ID
def get_next_ticket_id(tickets):
    if not tickets:
        return 1
    return max(ticket["ticket_id"] for ticket in tickets) + 1


# Create a ticket
def create_ticket():
    tickets = load_tickets()
    ticket_id = get_next_ticket_id(tickets)

    customer = input("Customer Name: ")
    email=input("enter your email:")
    issue = input("Issue Description: ")

    ticket = {
        "ticket_id": ticket_id,
        "customer_name": customer,
        "issue": issue,
        "status": "Open",
        "assigned_to": "Not Assigned"
    }

    tickets.append(ticket)
    save_tickets(tickets)
    print("✅ Ticket created successfully!")


# View all tickets
def view_tickets():
    tickets = load_tickets()
    if not tickets:
        print("No tickets available.")
        return

    for ticket in tickets:
        print("-" * 40)
        for key, value in ticket.items():
            print(f"{key}: {value}")


# Update a ticket
def update_ticket():
    tickets = load_tickets()
    ticket_id = int(input("Enter Ticket ID: "))

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            ticket["status"] = input("New Status (Open/In Progress/Closed): ")
            ticket["assigned_to"] = input("Assign to Agent: ")
            save_tickets(tickets)
            print("✅ Ticket updated successfully!")
            return

    print("❌ Ticket not found.")


# Close a ticket
def close_ticket():
    tickets = load_tickets()
    ticket_id = int(input("Enter Ticket ID to close: "))

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            ticket["status"] = "Closed"
            save_tickets(tickets)
            print("✅ Ticket closed successfully!")
            return

    print("❌ Ticket not found.")


# Menu
def menu():
    print("\nCustomer Support Ticket System")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Update Ticket")
    print("4. Close Ticket")
    print("5. Exit")


# Main program
def main():
    initialize_file()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            close_ticket()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
