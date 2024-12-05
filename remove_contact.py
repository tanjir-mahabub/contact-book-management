def remove_contact(contacts):
    """
    Removes a contact based on the phone number.
    """
    phone = input("Enter the Phone Number of the contact to remove: ").strip()

    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return

    print("Error: Contact not found.")
