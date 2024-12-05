def validate_contact(name, email, phone, address):
    """
    Validates the inputs for a new contact.
    """
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    if not name.isalpha():
        raise ValueError("Name must contain only letters.")
    if not phone.isdigit():
        raise ValueError("Phone number must contain only digits.")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address.")
    if not address.strip():
        raise ValueError("Address cannot be empty.")

def add_contact(contacts):
    """
    Adds a new contact to the contacts list.
    """
    try:
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        address = input("Enter Address: ").strip()

        # Validate inputs
        validate_contact(name, email, phone, address)

        # Check for duplicate phone numbers
        for contact in contacts:
            if contact['phone'] == phone:
                print("Error: Phone number already exists.")
                return

        # Add the new contact
        new_contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
        contacts.append(new_contact)
        print("Contact added successfully!")

    except ValueError as e:
        print(f"Error: {e}")
