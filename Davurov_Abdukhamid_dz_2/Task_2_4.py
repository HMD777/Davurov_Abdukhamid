def convert_name_extract(list_in: list) -> list:
    list_1 = []
    list_2 = []
    list_3 = []

    for i in list_in:
       list_1.append(i.split())
    for i in list_1:
       list_2.append(i[-1])
    for i in list_2:
        list_3.append (f'Привет, {str.capitalize(i)},!')

    list_out = (list_3)
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)

#['Привет, Игорь!', 'Привет, Марина!', 'Привет, Николай!', 'Привет, Аэлита!']