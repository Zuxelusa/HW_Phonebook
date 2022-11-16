from ui_input import *
from ui_view import *
from search import search
import time

PB_FILE = "phone.txt"

def read_base(file):
    print('Чтение')
    with open(file, 'r', encoding='utf-8') as text:
        last_id = int(text.readline().split('\n')[0])
        resultData = list()
        dict_contact = {}
        dict_phone = {}
        for line in text.readlines():
            list_record = line.split('\n')[0].split(';')
            dict_contact[int(list_record[0])] = list_record[1]
            dict_phone[int(list_record[0])] = list_record[2]
        resultData.append(dict_contact)
        resultData.append(dict_phone)
    return resultData, last_id

def save_base(file, base, last_id):
    print('Запись')
    with open(file, 'w', encoding='utf-8') as text:
        text.write(str(last_id)+'\n')
        for key in base[0].keys():
            text.write(str(key)+';'+base[0][key]+';'+base[1][key]+'\n')

def find_contact(base, last_id):
    find = input("Что ищем: ")
    print (search(find, base))
    return

def edit_contact(base, last_id):
    print('Редактирование')
    id = int(correct_input())
    if base[0].get(id, 0):
        while True:
            correct_menu()
            menu_item = menu_input()
            if menu_item == '3':
                base[1][id] += ' ' + \
                    input('Введите дополнительный номер телефона: ')
            elif menu_item == '2':
                base[1][id] = input('Введите правильный номер телефона: ')
            elif menu_item == '1':
                base[0][id] = input('Введите новое ФИО: ')
            elif menu_item == '0':
                break
            else:
                print('Такого пункта нет')
    else:
        print('Такого ID нет')
    return last_id


def new_contact(base, last_id):
    print('Новый контакт')
    name, phone = new_input()
    last_id += 1
    base[0][last_id] = name
    base[1][last_id] = phone
    return last_id


def del_contact(base, last_id):
    print('Удаление')
    id = int(del_input())
    if base[0].get(id, 0):
        base[0].pop(id)
        base[1].pop(id)
        # break
    else:
        print('Такого ID нет')
    # print(base)
    return last_id


def import_contacts():
    print('Импорт')
    return


def export_contacts(base,last_id):
    print('Экспорт')
    file=input('Введите имя файла экспорта: ')+'.html'
    with open(file, 'w', encoding='utf-8') as text:
        text.write(f'<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="UTF-8">\n')
        text.write(f'    <title>Телефонный справочник</title>\n</head >\n<body >\n   <table >\n')
        text.write(f'        <tr > <th > ID </th><th> ФИО </th><th> Телефоны </tr >\n')
        for key in base[0].keys():
            text.write(f'        <tr > <td > {key} <td > {base[0][key]} <td > {base[1][key]} </tr >\n')
        text.write(f'    </table >\n</body >\n</html >\n')
    return last_id


OPERATIONS = {
    "1": find_contact,
    "2": edit_contact,
   "3": new_contact,
   "4": del_contact,
   "5": import_contacts,
   "6": export_contacts
}


def choice(op, base, last_id):
    return OPERATIONS[op](base, last_id)

def log_add_note(event, description):
    with open("..\log.txt", "a", encoding="utf-8") as log:
        line = f"{time.strftime('%d-%m-%Y %H:%M:%S')};{event};{description}\n"
        log.write(line)

