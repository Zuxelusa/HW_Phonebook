# def read_base(file):
#     print('Чтение')
#     with open(file, 'r', encoding='utf-8') as text:
#         last_id=int(text.readline().split('\n')[0])
#         resultData = list()
#         dict_contact={}
#         dict_phone={}
#         for line in text.readlines():
#             list_record=line.split('\n')[0].split(';')
#             dict_contact[int(list_record[0])]=list_record[1]
#             dict_phone[int(list_record[0])]=list_record[2]
#         resultData.append(dict_contact)
#         resultData.append(dict_phone)
#     return resultData, last_id

# чтение содержимого справочника. возвращает кортеж двух словарей (fio и phones)
def read_base(file):
    print('Чтение')
    with open(file, 'r', encoding='utf-8') as text:
        # last_id=int(text.readline().split('\n')[0])
        resultData = list()
        dict_contact={}
        dict_phone={}
        for line in text.readlines():
            list_record=line.split('\n')[0].split(';')
            dict_contact[int(list_record[0])]=list_record[1]
            dict_phone[int(list_record[0])]=list_record[2]
        resultData.append(dict_contact)
        resultData.append(dict_phone)
    return resultData

 # определяет последний id в выгруженном справочнике
def last_baseid(result):
    return max(list(result[0].keys()))

# print(read_base_("phone_.txt"))
# print(last_baseid(read_base_("phone_.txt")))

def save_base(file,base,last_id):
    print('Запись')
    with open(file, 'w', encoding='utf-8') as text:
        text.write(str(last_id)+'\n')
        for key in base[0].keys():
            text.write(str(key)+';'+base[0][key]+';'+base[1][key]+'\n')

#апись полной измененной базы обратно в файл
def save_base_(file,base,last_id):
    print('Запись')
    with open(file, 'w', encoding='utf-8') as text:
        for key in base[0].keys():
            text.write(str(key)+';'+base[0][key]+';'+base[1][key]+'\n')

result = read_base("phone.txt")
save_base_("phone.txt", result, last_baseid(result))



# запись нового контакта в файл (base - кортеж из 2 элементов фио и телефоны)
# def new_contact(file,base,last_id):
#     print('Запись')
#     with open(file, 'a', encoding='utf-8') as text:
#         text.write(str(last_id) + ';' + base[0] + ';' + base[1] + '\n')

 # result = read_base("phone.txt")
 # save_base("phone.txt", ("ИИИ", "099090283"), last_baseid(result))

def find_contact():
    print('Поиск')
    return

def edit_contact():
    print('Редактирование')
    return

def new_contact():
    print('Новый контакт')
    return

def del_contact():
    print('Удаление')
    return

def import_contacts():
    print('Импорт')
    return

def export_contacts():
    print('Экспорт')
    return

OPERATIONS = {
   "1": find_contact,
   "2": edit_contact,
   "3": new_contact,
   "4": del_contact,
   "5": import_contacts,
   "6": export_contacts
}


def choice(op):
    OPERATIONS[op]()