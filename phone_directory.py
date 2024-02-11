import os
from typing import *

from config import Config


class PhoneDirectory:
    __PHONE_DIRECTORY_FILE = Config.PHONE_DIRECTORY_FILE
    __FIELDS = Config.FIELDS
    __instance = None
    __entries = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not os.path.exists(self.__PHONE_DIRECTORY_FILE):
            with open(self.__PHONE_DIRECTORY_FILE, "w"):
                pass
        with open(self.__PHONE_DIRECTORY_FILE, "r") as file:
            lines = file.readlines()
            self.__entries = [line.strip().split(";") for line in lines]
        super().__init__()

    def _save_file(self) -> None:
        with open(self.__PHONE_DIRECTORY_FILE, "w") as file:
            for entry in self.__entries:
                file.write(";".join(entry) + "\n")

    def print_directory_page(self, page_num, page_size) -> None:
        start_index = (page_num - 1) * page_size
        end_index = min(start_index + page_size, len(self.__entries))
        for entry in self.__entries[start_index:end_index]:
            self._print_entry(entry)
            print()

    @staticmethod
    def _print_entry(entry: List[str]) -> None:
        for field, value in zip(Config.FIELDS, entry):
            print(f"{field}: {value}")

    def add_entry_and_save_file(self) -> None:
        new_entry = []
        for field in self.__FIELDS:
            value = input(f"Введите {field}: ")
            new_entry.append(value)
        self.__entries.append(new_entry)
        self._save_file()
        print("Запись добавлена.")

    def edit_entry(self) -> None:
        query = input("Введите фамилию для редактирования: ")
        found_entries = []
        for entry in self.__entries:
            if entry[0].lower() == query.lower():
                found_entries.append(entry)
        if not found_entries:
            print("Запись не найдена.")
            return
        elif len(found_entries) > 1:
            print("Найдено несколько записей с такой фамилией. Выберите одну для редактирования:")
            for i, entry in enumerate(found_entries):
                print(f"{i + 1}.")
                self._print_entry(entry)
                print()
            choice = int(input()) - 1
            entry_to_edit = found_entries[choice]
        else:
            entry_to_edit = found_entries[0]
        print("Текущая запись:")
        self._print_entry(entry_to_edit)
        print()
        for i, field in enumerate(self.__FIELDS):
            new_value = input(
                f"Введите новое значение для {field} (или оставьте пустым для сохранения текущего значения): ")
            if new_value:
                entry_to_edit[i] = new_value
        self._save_file()
        print("Запись отредактирована.")

    def search_entries(self):
        query = input("Введите фамилию для поиска: ")
        found_entries = []
        for entry in self.__entries:
            if query.lower() in entry[0].lower():
                found_entries.append(entry)
        if not found_entries:
            print("Записи не найдены.")
        else:
            print("Найденные записи:")
            for entry in found_entries:
                self._print_entry(entry)
                print()
