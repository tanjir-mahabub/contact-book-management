def search_contact(contacts):
    """
    Searches for contacts based on a query (name, email, or phone).
    """
    query = input("Enter Name, Email, or Phone to search: ").strip().lower()
    
    results = [
        contact for contact in contacts
        if query in contact['name'].lower() or
           query in contact['email'].lower() or
           query in contact['phone']
    ]

    if not results:
        print("No contacts found.")
        return

    print("\nSearch Results:")
    print("{:<20} {:<30} {:<15} {:<30}".format("Name", "Email", "Phone", "Address"))
    print("-" * 95)
    for contact in results:
        print("{:<20} {:<30} {:<15} {:<30}".format(
            contact['name'], contact['email'], contact['phone'], contact['address']
        ))
