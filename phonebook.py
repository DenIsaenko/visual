import json
from typing import List


class Contact:
    def __init__(
        self,
        last_name: str,
        first_name: str,
        middle_name: str,
        organization: str,
        work_phone: str,
        personal_phone: str,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone


class PhoneBook:

    def read_contacts(self)->List[Contact]:
        '''Чтение контактов из файла'''
        contacts = []
        try:
            with open("phonebook.json", "r", encoding='utf-8') as file:
                contacts_data = json.load(file)
            contacts = [Contact(*data.values()) for data in contacts_data]
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return contacts

    def add_contact(self, contact: Contact) -> None:
        '''Добавление контакта'''
        contacts = self.read_contacts()
        contacts.append(contact)
        self.save_contacts(contacts)
        print("Новая запись успешно добавлена")

    def edit_contact(self, index: int, contact:Contact)->None:
        '''Редактирование записей'''
        contacts = self.read_contacts()
        if 0 <= index < len(contacts):
            contacts[index] = contact
            self.save_contacts(contacts)
            print("Запись успешно отредактирована")
        else:
            print("Некорректный номер записи")

    def save_contacts(self, contacts: List[Contact])->None:
        '''Сохранение контактов в файл'''
        contacts_data = [contact.__dict__ for contact in contacts]
        with open("phonebook.json", "w", encoding='utf-8') as file:
            json.dump(contacts_data, file, indent=4)

    def search_contacts(self, search_params: List[str])->List[Contact]:
        contacts = self.read_contacts()
        results = []
        for contact in contacts:
            if all(
                param.lower() in contact.__dict__.values() for param in search_params
            ):
                results.append(contact)
        return results
