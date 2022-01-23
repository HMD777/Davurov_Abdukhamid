


sec_in_day = 86400  # 84600 sec in 1 day
sec_in_hour = 3600  # 3600 sec in 1 hour
sec_in_min = 60     # 60 sec in 1 min


def convert_time(duration: int) -> str:
    day_result = 0
    hour_result = 0
    min_result = 0
    sec_result = 0
    while duration >= sec_in_day:
        day_result = duration // sec_in_day
        duration = duration-(day_result*sec_in_day)
    while duration >= sec_in_hour:
        hour_result =duration//sec_in_hour
        duration = duration-(hour_result*sec_in_hour)
    while duration >= sec_in_min:
        min_result = duration // sec_in_min
        duration = duration-(min_result*sec_in_min)
    while (duration > 0):
        duration -= 1
        sec_result += 1

    if day_result > 0:
        result=(f'{day_result} дн {hour_result} час {min_result} мин {sec_result} сек')
    elif (day_result == 0) and (hour_result > 0):
        result=(f'{hour_result} час {min_result} мин {sec_result} сек')
    elif (day_result == 0) and (hour_result == 0) and (min_result > 0):
        result = (f'{min_result} мин {sec_result} сек')
    elif (day_result == 0) and (hour_result == 0) and (min_result == 0) and (sec_result > 0):
        result = (f'{sec_result} сек')
    else:
        result = ("Введено не правильные данные!")
    return result

duration = int(input('Duration '))
result = convert_time(duration)
print(result)
