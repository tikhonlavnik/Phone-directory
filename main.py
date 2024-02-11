from phone_directory import PhoneDirectory


def main():
    directory = PhoneDirectory()
    page_size = 5
    while True:
        print("\nТелефонный справочник")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            page_num = int(input("Введите номер страницы: "))
            directory.print_directory_page(page_num, page_size)
        elif choice == "2":
            directory.add_entry_and_save_file()
        elif choice == "3":
            directory.edit_entry()
        elif choice == "4":
            directory.search_entries()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
