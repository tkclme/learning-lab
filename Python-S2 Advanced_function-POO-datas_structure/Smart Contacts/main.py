from core.addressBook import AddressBook

from interface.inferface import get_info

from core.controller import add_new_contact

from const import TITLE, RECORDED, INFOS_REQUEST, PATH



"""
Chaque contact est un objet avec nom, prénom, email, téléphone.

Tu peux ajouter, supprimer, rechercher un contact.

Utilise un dictionnaire pour stocker les contacts avec des méthodes bien pensées.

Bonus : ajoute des filtres (par nom, par domaine d’email), sauvegarde en JSON.

"""


def main():
    smart_addr_book = AddressBook()
    smart_addr_book.load(PATH)

    while True:
        n_contacts = len(smart_addr_book.contact_list)
        print(TITLE)
        print(n_contacts, RECORDED)
        smart_addr_book.diplay()
        add_new_contact(smart_addr_book, get_info, INFOS_REQUEST)
        smart_addr_book.save(PATH)


if __name__ == "__main__":
    main()
