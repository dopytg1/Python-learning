KEY_VALUE_DELIMETR = "----"
KEY_VALUE_PAIR_DELIMETR = "****"

def read_from_file():
    contacts = []
    with open('contacts.txt', 'r') as f:
        contacts_data = f.readlines()
        print(contacts_data)
        for contact_data in contacts_data:
            contact_data = contact_data.strip()
            contact = {}
            for key_value in contact_data.split(KEY_VALUE_PAIR_DELIMETR):
                key, value = key_value.split(KEY_VALUE_DELIMETR)
                contact[key] = value
            contacts.append(contact)

    return contacts

contacts = read_from_file()

def write_to_file():
    contacts_data = []
    for contact in contacts:
        contact_data = []
        for key, value in contact.items():
            contact_data.append(f'{key}{KEY_VALUE_DELIMETR}{value}')
        contacts_data.append(KEY_VALUE_PAIR_DELIMETR.join(contact_data))
    with open('contacts.txt', 'w') as f:
        f.write('\n'.join(contacts_data))



def check_delimetr(text):
    for delimetr in (KEY_VALUE_DELIMETR, KEY_VALUE_PAIR_DELIMETR):
        if delimetr in text:
            print(f"не вводите {(KEY_VALUE_DELIMETR, KEY_VALUE_PAIR_DELIMETR)}")
            return False
    return True


def sort_by_name():
    def keyFunc(item):
        return item['name']

    contacts.sort(key = keyFunc, reverse=False)
    write_to_file()


def print_contact(contact):
    print("%-25s %s" % (contact['name'], contact['phone']))

def get_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

def list_contacts():
    sort_by_name()
    print("%-25s %s" % ("Name","Phone"))
    print("-" * 35)
    for contact in contacts:
        print_contact(contact)


def find_contact():
    name = input("Введите имя контакта который вы хотите найти: ")
    contact = get_contact(name)
    if contact:
        print_contact(contact)
    else:
        print("Нет такого контакта")

def add_contact():
    name = input("Введите имя контакта который хотите добавить: ")
    contact = get_contact(name)
    if contact:
        print("Такой контакт уже есть.")
    else:
        if check_delimetr(name):
            phone = input("Введите номер телефона: ")
            if check_delimetr(phone):
                new_contact = {"name": name.capitalize(), "phone": phone}
                contacts.append(new_contact)
                write_to_file()

def edit_contact():
    name = input("Введите имя контакта который хотите изменить: ")
    contact = get_contact(name)
    if not contact:
        print("Такого контакта нет")
    else:
        new_name = input("Введите новое имя: ").capitalize()
        if check_delimetr(new_name):
            new_phone = input("Введите новый номер: ")
            if check_delimetr(new_phone):
                contact['name'] = new_name
                contact['phone'] = new_phone
                write_to_file()

def delete_contact():
    name = input("Введите имя контакта который хотите удалить: ")
    contact = get_contact(name)
    if not contact:
        print("Такого контакта нет")
    else:
        answer = input("Вы уверены что хотите удалить '%s': " % contact['name'])
        if answer.lower() in ('yes',"ok","да", 'y'):
            contacts.remove(contact)
            write_to_file()


def get_menu():
    print('''list - вывести контакты
find - найти контакт
add - добавить контакт
edit - изменить контакт
delete - удалить контакт
exit - выход''')

def main():
    while True:
        get_menu()
        command = input("Введите команду: ").lower()
        if command == "exit":
            break
        elif command == "list":
            list_contacts()
        elif command == "find":
            find_contact()
        elif command == "add":
            add_contact()
        elif command == "edit":
            edit_contact()
        elif command == "delete":
            delete_contact()
        else:
            print("Такой команды нет")

main()