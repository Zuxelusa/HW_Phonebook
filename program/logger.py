'''
файл лога: log.txt (одна строка 1 запись, разделитель полей -табуляция (\t))
функция
на входе: СОБЫТИЕ, ОПИСАНИЕ (строка с описанием события)
на выходе: дозапись в лог DATASTAMP, СОБЫТИЕ, ОПИСАНИЕ

'''
import time
def log_add_note(event, description):
    with open("..\log.txt", "a", encoding="utf-8") as log:
        line = f"{time.strftime('%d-%m-%Y %H:%M:%S')};{event};{description}\n"
        log.write(line)
