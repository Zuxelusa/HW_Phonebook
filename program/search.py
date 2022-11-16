
1. Поиск контакта по любым данным       (search)

Функция
на входе: любая строка str для поиска
действие: производит поиск всех вхождений, найденных в БД
ны выходе: все найденные записи в виде строк, слоа, в которых было найдено вхождение, 
можно подсветить цветом
'''

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
