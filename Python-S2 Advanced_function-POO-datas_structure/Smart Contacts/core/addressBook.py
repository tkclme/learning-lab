from core.contact import Contact
import json

class AddressBook:
    def __init__(self):
        self.contact_list = []


    def add(self, new_contact):
        self.contact_list.append(new_contact)


    def delete(self, contact):
        if contact in self.contact_list:
            delete_contact = self.contact_list.pop(contact)


    def diplay(self):
        if self.contact_list:
            for contact in self.contact_list:
                print(f"- {contact.name}")


    def save(self, path):
        with open(path, "w", encoding="utf-8") as json_file:
            data = []
            for contact in self.contact_list:
                data.append(contact.to_dict())
            json.dump(data, json_file, indent=2)

    def load(self, path):
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        for entry in data:
            loading_contact = Contact(entry)
            self.add(loading_contact)
