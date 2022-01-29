
dict_one_to_ten = {
    "one": 'один',
    "two": 'два',
    "three": 'три',
    "four": 'четыре',
    "five": 'пять',
    "six": 'шесть',
    "seven": 'семь',
    "eight": 'восемь',
    "nine": 'девять',
    "ten": 'десять'
}


def num_translate(value: str) -> str:

    if value in dict_one_to_ten:
        result = dict_one_to_ten[value]
    else:
        result = "None"

    str_out = f'"{result}"'
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("eleven"))