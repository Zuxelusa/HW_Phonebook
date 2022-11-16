from action import*
from ui_input import menu_input, check_menu_item, input_value, input_op
from ui_view import menu, print_char, print_memory

base,last_id=read_base('phone.txt')
# print(type(base))
while True:
    menu()
    menu_item = menu_input()
    if not check_menu_item(menu_item):
        # обработка неправильного выбора меню
        print('Такого пункта нет')
        continue
    elif menu_item=='0': break
    last_id=choice(menu_item,base,last_id)
save_base('phone.txt',base,last_id)


