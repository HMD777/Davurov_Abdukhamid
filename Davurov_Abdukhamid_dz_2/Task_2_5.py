import math
from random import uniform

def transfer_list_in_str(list_in: list) -> str:
   list_new = []

   for i in list_in:
       rub=0
       cent=0
       if math.floor(i)>0:
           rub=math.floor(i)
           cent = round((i - math.floor(i))*100)
       elif math.floor(i)==0:
           rub =0
           cent = round((i - math.floor(i))*100)
       list_new.append(f"{rub} руб {cent:02} коп")
   str_out = list_new
   return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

#------------------------------------------------------------------------------

def sort_prices(list_in: list) -> list:

    list_new = []

    for i in list_in:
        rub = 0
        cent = 0
        if math.floor(i) > 0:
            rub = math.floor(i)
            cent = round((i - math.floor(i)) * 100)
        elif math.floor(i) == 0:
            rub = 0
            cent = round((i - math.floor(i)) * 100)
        list_new.append(f"{rub} руб {cent:02} коп")

    return sorted(list_new)


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)

#---------------------------------------------------------------------
def sort_price_adv(list_in: list) -> list:
    list_new = []

    for i in list_in:
        rub = 0
        cent = 0
        if math.floor(i) > 0:
            rub = math.floor(i)
            cent = round((i - math.floor(i)) * 100)
        elif math.floor(i) == 0:
            rub = 0
            cent = round((i - math.floor(i)) * 100)
        list_new.append(f"{rub} руб {cent:02} коп")

    list_out = sorted(list_new, reverse=True)
    return list_out

result_3 = sort_price_adv(my_list)
print(result_3)

#------------------------------------------------
def check_five_max_elements(list_in: list) -> list:
    list_new = []

    for i in list_in:
        rub = 0
        cent = 0
        if math.floor(i) > 0:
            rub = math.floor(i)
            cent = round((i - math.floor(i)) * 100)
        elif math.floor(i) == 0:
            rub = 0
            cent = round((i - math.floor(i)) * 100)
        list_new.append(f"{rub} руб {cent:02} коп")

    list_out = sorted(list_new, reverse=True)
    return list_out[:5]
result_4 = check_five_max_elements(my_list)
print(result_4)
