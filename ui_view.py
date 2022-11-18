import action

MENU_ITEMS = {
   "1": "Поиск",
   "2": "Редактирование",
   "3": "Новый контакт",
   "4": "Удаление",
   "5": "Импорт",
   "6": "Экспорт",
   "0": "Выход"
}

def print_memory():
    print(f"Число в памяти: {action.memory}")

def menu():
    print("\nТЕЛЕФОННЫЙ СПРАВОЧНИК\n")
    print(action.list_view_PB(), "\n")
    print("МЕНЮ:")
    for index, item in MENU_ITEMS.items():
        print(f"{index} - {item}")
    print("Выберите пункт меню: ", end="")

MENU_CORRECT = {
   "1": "ФИО",
   "2": "Телефон",
   "3": "Добавить телефон",
   "0": "Выход"
}

def correct_menu():
    for index, item in MENU_CORRECT.items():
        print(f"{index} - {item}")
    print("Выберите пункт меню: ", end="")


def print_char(ch):
    print(f"Введите {ch}: ", end="")

def search_title():
    print("\nПоиск по телефонному справочнику.")
    print("\nЧто ищем: ", end="")

