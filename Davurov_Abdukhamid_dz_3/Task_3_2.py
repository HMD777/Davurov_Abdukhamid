
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



def num_translate_adv(value: str) -> str:
    cond_uc = bool
    if str.isupper(value[0]) is True:
        value_new = str.lower(value)
        cond_uc = True
    else:
        value_new = value

    if value_new in dict_one_to_ten:
        if cond_uc is True:
            result = str.capitalize(dict_one_to_ten[value_new])
        else:
            result = dict_one_to_ten[value_new]
    else:
        result = "None"

    str_out = f'"{result}"'
    return str_out


print(num_translate_adv("one"))
print(num_translate_adv("Eight"))
print(num_translate_adv("eleven"))
