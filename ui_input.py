from ui_view import MENU_ITEMS


def menu_input():
    """
    Ф-ция получает от пользователя выбранный пункт меню
    :return: число, пункт меню
    """
    return input()

def del_input():
    """
    Ф-ция получает от пользователя id удаляемого элемента
    :return: число, id
    """
    return input('Ведите ID удаляемой записи: ')

def correct_input():
    """
    Ф-ция получает от пользователя id корректируемого элемента
    :return: число, id
    """
    return input('Ведите ID корректируемой записи: ')

def new_input():
    """
    Ф-ция получает от пользователя ФИО и телефон нового контакта
    :return: число, id
    """
    name=input('Ведите ФИО: ')
    phone=input('Введите номер телефона: ')
    return name, phone 


def check_menu_item(menu_item):
    """
    Ф-ция проверяет корректность выбранного пункта меню
    :param menu_item:
    :return: логическое значение
    """
    return bool(MENU_ITEMS.get(menu_item))


def input_value():
    return int(input()) # TODO: выполнить проверку если число

def input_op():
    return input()  # TODO: выполнить проверку если допустимая операция