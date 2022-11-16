'''
1. Поиск контакта по любым данным       (search)
Функция
на входе: любая строка str для поиска
действие: производит поиск всех вхождений, найденных в БД
ны выходе: все найденные записи в виде строк, слоа, в которых было найдено вхождение, 
можно подсветить цветом
'''

# функция произодит поиск всех вхождений в любых полях и на выходе выдает список в таком же формате.
def search(base, last_id):
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