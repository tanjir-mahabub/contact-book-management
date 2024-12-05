def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\nSaved Contacts:")
    print("{:<20} {:<30} {:<15} {:<30}".format("Name", "Email", "Phone", "Address"))
    print("-" * 95)
    for contact in contacts:
        print("{:<20} {:<30} {:<15} {:<30}".format(
            contact['name'], contact['email'], contact['phone'], contact['address']
        ))
