'''
5. Экспорт контактов (CSV, JSON, HTML)  (convert)
Функции:
На входе: файл источника в TXT (с табуляцией)
На выходе: файл с тем же именем в выбранном формате.
'''
from convert_rules import CSV
from convert_rules import HTML

def convert_to_csv(sou_file):
    f_s = open(sou_file, "r")
    res_file = sou_file.split('.')[-1] + ".csv"
    f_r = open(res_file, "w")
    while True:
        current = f_s.readline()
        if not current:
            break
        f_r.writelines(CSV(current))
    f_s.close()
    f_r.close()

def convert_to_html(sou_file):
    f_s = open(sou_file, "r")
    res_file = sou_file.split('.')[-1] + ".html"
    f_r = open(res_file, "w")
    f_r.writelines("<html>\n<head>PHONEBOOK</head>\n<body>\n<table>\n")
    f_r.writelines("<th><td>ID</td><td>NAME</td><td>PHONES</td></th>")
    while True:
        current = f_s.readline()
        if not current:
            break
        f_r.writelines(f"{HTML(current)}")
    f_r.writelines("</table>\n</body>")
    f_s.close()
    f_r.close()

convert_to_html("..\phone.txt")
convert_to_csv("..\phone.txt")