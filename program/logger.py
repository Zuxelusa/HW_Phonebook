'''
файл лога: log.txt (одна строка 1 запись, разделитель полей -табуляция (\t))
функция
на входе: СОБЫТИЕ, ОПИСАНИЕ (строка с описанием события)
на выходе: дозапись в лог DATASTAMP, СОБЫТИЕ, ОПИСАНИЕ

'''

def log_add_note(event, description):
    with open("log.txt", "a"):

    return