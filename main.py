from add_contact import add_contact
from view_contacts import view_contacts
from remove_contact import remove_contact
from search_contact import search_contact
from file_operations import load_contacts, save_contacts

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        # elif choice == '3':
        #     search_contact(contacts)
        # elif choice == '4':
        #     remove_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
