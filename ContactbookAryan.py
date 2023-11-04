class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print('-' * 20)

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, search_term, new_contact):
        for i, contact in enumerate(self.contacts):
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
                self.contacts[i] = new_contact
                return True
        return False

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
                self.contacts.remove(contact)
                return True
        return False

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                for contact in found_contacts:
                    print(f"Name: {contact.name}")
                    print(f"Phone: {contact.phone}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    print('-' * 20)
            else:
                print("No contacts found.")

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                new_contact = Contact(name, phone, email, address)
                if contact_book.update_contact(search_term, new_contact):
                    print("Contact updated successfully.")
                else:
                    print("Contact not found.")
            else:
                print("No contacts found.")

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            if contact_book.delete_contact(search_term):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
