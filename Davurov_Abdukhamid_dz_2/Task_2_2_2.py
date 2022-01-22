def convert_list_in_str(list_in: list) -> str:
    task_new = []
    for i in list_in:
        if not i.isalpha():
            task_new.append(f'"{i}"')
        else:
            task_new.append(i)

    str_out = " ".join(task_new)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

#в "05" часов "17" минут температура воздуха была "+05" градусов
