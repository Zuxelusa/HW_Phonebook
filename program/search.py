'''
1. Поиск контакта по любым данным       (search)

Функция
на входе: любая строка str для поиска
действие: производит поиск всех вхождений, найденных в БД
ны выходе: все найденные записи в виде строк, слоа, в которых было найдено вхождение, 
можно подсветить цветом
'''


base = [{1: 'Григоркин Алексей Васильевич', 2: 'Соловьёв Александр', 3: 'Тишкина Оксана', 4: 'Сергей'}, {1: '+79025153208 +79213456790', 2: '+79512345678', 3: '+79045678088', 4: '+74541324'}]

# функция произодит поиск всех вхождений в любых полях и на выходе выдает список в таком же формате.
def search(find: str, base):
    res = []
    res_ids = []
    for i in base:
        for j in i.items():
            if find in j[1]:
                 res_ids.append(j[0])

    res_ids = set(res_ids)

    for i in base:
        dict_tmp = {}
        for k in range(len(i)):
            for j in res_ids:
                dict_tmp[j] = i.get(j)
        res.append(dict_tmp)

    return res

# функция возвращает True если искомое вхождение найдено в базе.
def is_data(find, base):
    if not search(find, base)[0]: return False
    return True

    """Алгоритм поиска"""
def retrive(id='', name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result
