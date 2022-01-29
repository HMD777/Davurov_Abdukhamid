

def thesaurus(*args) -> dict:
    dict_out = {}
    i=0
    while i< len(args):
        if (args[i][0]) in dict_out:
            dict_added = []
            dict_added.append(dict_out[args[i][0]])
            dict_added.append(args[i])
            dict_out.update({args[i][0]: dict_added})
        dict_out.setdefault(args[i][0], args[i])
        i+=1
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))





"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
 в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

Например:

>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"],
    "П": ["Петр"]
}
Подумайте:

полезен ли будет вам оператор распаковки?
Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
ВНИМАНИЕ! Используйте стартовый код для своей реализации
"""
