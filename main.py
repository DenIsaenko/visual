from typing import List

from phonebook import Contact, PhoneBook


def display_contacts(contacts: List[Contact])->None:
    '''Вывод контактов на экран'''
    for contact in contacts:
        print(
            f"Фамилия:{contact.last_name} Имя:{contact.first_name} Отчество{contact.middle_name}, "
            f"Организация:{contact.organization}, Рабочий номер:{contact.work_phone}, Личный номер:{contact.personal_phone}"
        )


def add_contact(phone_book: PhoneBook)->None:
    '''Добавление контакта'''
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    organization = input("Введите название организации: ")
    work_phone = input("Введите рабочий телефон: ")
    personal_phone = input("Введите личный телефон: ")
    contact = Contact(
        last_name, first_name, middle_name, organization, work_phone, personal_phone
    )
    phone_book.add_contact(contact)


def edit_contact(phone_book: PhoneBook)->None:
    '''Редактирование контакта'''
    contacts = phone_book.read_contacts()
    display_contacts(contacts)
    index = int(input("Введите номер записи, которую нужно отредактировать: "))
    if 0 <= index < len(contacts):
        last_name = input("Введите новую фамилию: ")
        first_name = input("Введите новое имя: ")
        middle_name = input("Введите новое отчество: ")
        organization = input("Введите новое название организации: ")
        work_phone = input("Введите новый рабочий телефон: ")
        personal_phone = input("Введите новый личный телефон: ")
        contact = Contact(
            last_name, first_name, middle_name, organization, work_phone, personal_phone
        )
        phone_book.edit_contact(index, contact)
    else:
        print("Некорректный номер записи")


def search_contacts(phone_book: PhoneBook)->None:
    '''Поиск контакта'''
    search_params = (
        input("Введите одну или несколько характеристик для поиска (через запятую): ")
        .lower()
        .split(",")
    )
    results = phone_book.search_contacts(search_params)
    if results:
        print("Результаты поиска:")
        display_contacts(results)
    else:
        print("Поиск не дал результатов")


def main()->None:
    phone_book = PhoneBook()

    while True:
        print("Меню:")
        print("1. Вывести записи на экран")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            contacts = phone_book.read_contacts()
            display_contacts(contacts)
        elif choice == "2":
            add_contact(phone_book)
        elif choice == "3":
            edit_contact(phone_book)
        elif choice == "4":
            search_contacts(phone_book)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
