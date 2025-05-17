from const import INFO_CMD
from core.contact import Contact

def add_new_contact(addrBook, get_info, request):
    """Create new Contact class and add it into an AddressBook class.
    get_info() function generate a dict from a request with contact required attributes.
    """
    new_contact = Contact(get_info(request))
    addrBook.add(new_contact)


def search_contact(addrBook, contact_name):
    for contact in addrBook.contact_list:
        if contact_name == contact.name:
            return contact


def display_help():
    print(INFO_CMD)
    input("\nPress enter to continue")

