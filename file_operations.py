import os

FILE_NAME = "contacts.csv"

def load_contacts():
    """
    Loads contacts from a CSV file without using the `csv` library.
    Returns a list of dictionaries.
    """
    contacts = []
    
    if not os.path.exists(FILE_NAME):
        return contacts

    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        # Skip the header row
        lines = file.readlines()[1:]
        
        # Parse each line into a contact dictionary
        for line in lines:
            name, email, phone, address = line.strip().split(',')
            contacts.append({
                'name': name,
                'email': email,
                'phone': phone,
                'address': address
            })
    return contacts



def save_contacts(contacts):
    """
    Saves contacts to a CSV file without using the `csv` library.
    """
    with open(FILE_NAME, mode='w', encoding='utf-8') as file:
        # Write the header row
        file.write("name,email,phone,address\n")
        
        # Write each contact
        for contact in contacts:
            line = f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n"
            file.write(line)
