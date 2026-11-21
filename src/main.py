from manager import ComplaintManager


def display_menu():
    print("\n===================================")
    print(" COLLEGE GRIEVANCE MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Register a Complaint")
    print("2. View All Complaints")
    print("3. Search Complaint")
    print("4. Update Complaint Status")
    print("5. Exit")


def main():
    manager = ComplaintManager()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Student name (leave blank for anonymous): ")
            category = input("Complaint category: ")
            description = input("Complaint description: ")

            complaint_id = manager.register_complaint(
                category,
                description,
                name if name else "Anonymous"
            )

            print(f"\nComplaint registered successfully!")
            print(f"Your Complaint ID: {complaint_id}")

        elif choice == "2":
            complaints = manager.view_complaints()

            if not complaints:
                print("\nNo complaints found.")
            else:
                for complaint in complaints:
                    print("\n---------------------------")
                    for key, value in complaint.items():
                        print(f"{key}: {value}")

        elif choice == "3":
            complaint_id = input("Enter Complaint ID: ")
            complaint = manager.search_complaint(complaint_id)

            if complaint:
                print("\nComplaint Details:")
                for key, value in complaint.items():
                    print(f"{key}: {value}")
            else:
                print("\nComplaint not found.")

        elif choice == "4":
            complaint_id = input("Enter Complaint ID: ")
            status = input("Enter new status (Pending/Under Review/Resolved): ")

            if status not in ["Pending", "Under Review", "Resolved"]:
                print("\nInvalid status.")
            elif manager.update_status(complaint_id, status):
                print("\nComplaint status updated successfully.")
            else:
                print("\nComplaint not found.")

        elif choice == "5":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
