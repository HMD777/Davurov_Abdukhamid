

def transform_string(number: int) -> str:
    if number == 1:
        text = f'{number} процент'
    elif 1 < number % 10 and number % 10 < 5:
        text = f'{number} процента'
    elif number % 10 == 1:
        text = f'{number} процент'
    else:
        text = f'{number} процентов'
    return text


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))