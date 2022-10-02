#  Дико извиняюсь за то что вам приходится проверять код без комментариев.
#  Еле успел доделать допы сегодня, а время уже 18:56.

contacts = [
    {
        "name": 'John',
        "phone": '123456'
    },
    {
        "name": 'Jane',
        "phone": '654321'
    },
    {
        "name": 'Bob',
        "phone": '+1234'
    },
]

def sort_contact():
    def keyFunc(item):
        return item['name']

    contacts.sort(key = keyFunc)
    for i in range(len(contacts)):
        print("%-30s %s" %(contacts[i]['name'], contacts[i]['phone']))


def find():
    searchingFor = input("Name: ")
    for i in range(len(contacts)):
        if searchingFor == contacts[i]['name']:
            return contacts[i]


def print_contact():
    for i in range(len(contacts)):
        print("%-25s %s" %(contacts[i]['name'], contacts[i]['phone']))


def find_contact():
    searchedCont = find()
    if searchedCont != None:
        print("%-25s %s" %(searchedCont['name'], searchedCont['phone']))
    else:
        print("contact not found")


def add_contact():
    newContact = {}
    name = input("Name: ")
    phone = input("Phone: ")
    
    confirm = 0
    for i in range(len(contacts)):
        for key, values in contacts[i].items():
            if name == values:
                confirm = True
                break

    if not confirm:
        newContact['name'] = name
        newContact['phone'] = phone
        contacts.append(newContact) 
    else:
        del newContact
        print("Contact already in list")
        

def edit_contact():
    searchedCont = find()
    if searchedCont != None:
        newName = input("Write a new name:")
        newPhone = input("Write a new phone number:")
        searchedCont['name'] = newName
        searchedCont['phone'] = newPhone
    else:
        print("contact not found")


def delete_contact():
    searchedCont = find()
    if searchedCont != None:
        confirm = input("Are you sure you want to delete a contact? yes/no: ")
        if confirm == 'yes':
            for i in range(len(contacts)):
                if searchedCont == contacts[i]:
                    del contacts[i]
                    break
        else:
            pass

    
while True:
    command = input("Enter something from (list, find, add, delete, edit, sort or exit): ")
    if command == 'list':
        print_contact()
    elif command == 'find':
        find_contact()
    elif command == 'add':
        add_contact()
    elif command == 'delete':
        delete_contact()
    elif command == 'edit':
        edit_contact()
    elif command == 'sort':
        sort_contact()
    elif command == 'exit':
        break
    else:
        print("try again")
        pass