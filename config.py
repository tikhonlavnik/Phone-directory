from typing import List


class Config:
    PHONE_DIRECTORY_FILE: str = "phone_directory_database.txt"
    FIELDS: List[str] = ["Фамилия", "Имя", "Отчество", "Организация", "Рабочий телефон", "Личный телефон"]
