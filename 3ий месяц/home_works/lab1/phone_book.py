from operator import ne
from typing import List, Optional
import json

class Contact:
    def __init__(self, name: str , phone: str) -> None:
        self.name = name.capitalize()
        self.phone = phone

    def print_contact(self):
        print(f"{self.name:<20}{self.phone:>15}")

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

    def edit_contact(self, new_name: str, new_phone: str):
        self.name = new_name.capitalize()
        self.phone = new_phone

contact = Contact("John", "+4132412421")

class PhoneBook:
    def __init__(self, contacts: Optional[List[Contact]] = None):
        self.contacts = contacts if contacts else []

    def print_contacts(self):
        print(f"{'Name':<20}{'Phone':>15}")
        print("-" * 35)
        self.contacts.sort(key=lambda contact: contact.name)
        for contact in self.contacts:
            contact.print_contact()

    def add_contact(self, new_contact: Contact):
        self.contacts.append(new_contact)

    def remove_contact(self, contact: Contact):
        self.contacts.remove(contact)

    def get_contact(self, name: str)-> Optional[Contact]:
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact

class Application:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.phone_book = PhoneBook(self.read_from_file())

    def read_from_file(self)-> List[Contact]:
        with open(self.file_path, 'r') as f:
            contacts: List[Contact] = []
            contacts_data = f.read()
            if contacts_data:
                for contact_dict in json.loads(contacts_data):
                    contact = Contact(contact_dict['name'], contact_dict['phone'])
                    contacts.append(contact)
            return contacts

    def write_to_file(self):
        with open(self.file_path, 'w') as f:
            contacts_data = []
            for contact in self.phone_book.contacts:
                contacts_data.append(contact.to_dict())
            json.dump(contacts_data, f, indent=4)

    def command_list(self):
        self.phone_book.print_contacts()

    def command_find(self):
        name = input("Введите имя контакта который вы хотите найти: ")
        contact = self.phone_book.get_contact(name)
        if contact:
            contact.print_contact()
        else:
            print("Нет такого контакта")

    def command_add(self):
        name = input("Введите имя контакта который хотите добавить: ")
        contact = self.phone_book.get_contact(name)
        if contact:
            print("Такой контакт уже есть.")
        else:
            phone = input("Введите номер телефона: ")
            new_contact = Contact(name, phone)
            self.phone_book.add_contact(new_contact)
            self.write_to_file()

    def command_delete(self):
        name = input("Введите имя контакта который хотите удалить: ")
        contact = self.phone_book.get_contact(name)
        if not contact:
            print("Такого контакта нет")
        else:
            answer = input("Вы уверены что хотите удалить '%s': " % contact.name)
            if answer.lower() in ('yes',"ok","да", 'y'):
                self.phone_book.remove_contact(contact)
                self.write_to_file()

    def command_edit(self):
        name = input("Введите имя контакта который хотите изменить: ")
        contact = self.phone_book.get_contact(name)
        if not contact:
            print("Такого контакта нет")
        else:
            new_name = input("Введите новое имя: ")
            if not new_name:
                new_name = contact.name
            elif self.phone_book.get_contact(new_name):
                print("Такой контакт уже есть.")
                return
            new_phone = input("Введите новый номер: ")
            contact.edit_contact(new_name,new_phone)
            self.write_to_file()


    @staticmethod
    def get_menu():
        print('''list - вывести контакты
find - найти контакт
add - добавить контакт
edit - изменить контакт
delete - удалить контакт
exit - выход''')

    def main(self):
        while True:
            Application.get_menu()
            command = input("Введите команду: ").lower()
            if command == "exit":
                break
            elif command == "list":
                self.command_list()
            elif command == "find":
                self.command_find()
            elif command == "add":
                self.command_add()
            elif command == "edit":
                self.command_edit()
            elif command == "delete":
                self.command_delete()
            else:
                print("Такой команды нет")
            

app = Application('contacts.json')
app.main()