
from random import randint, sample


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:

    list_out = []
    for i in range(count):
        list_out.append(f'{nouns[randint(1, len(nouns)-1)]} {adverbs[randint(1, len(adverbs) - 1)]} '
                        f'{adjectives[randint(1, len(adjectives) - 1)]}')
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
# def get_jokes_adv(...) -> list:
#     # пишите реализацию здесь
#     return []
def get_jokes_adv(count: int, **kwargs) -> list:
    list_out = []
    reason = kwargs.get('repeat', False)
    if reason is True:
        for i in range(count):
            list_out.append(f'{nouns[randint(1, len(nouns) - 1)]} '
                            f'{adverbs[randint(1, len(adverbs) - 1)]} '
                            f'{adjectives[randint(1, len(adjectives) - 1)]}')
    else:
        new_nouns = []
        new_nouns.extend(sample(nouns, k=len(nouns)))
        new_adverbs = []
        new_adverbs.extend(sample(adverbs, k=len(adverbs)))
        new_adjectives = []
        new_adjectives.extend(sample(adjectives, k=len(adjectives)))
        for i in range(count):
            if count <= len(nouns) <= len(adverbs) <= len(adjectives):
                list_out.append(f'{new_nouns[i]} '
                                f'{new_adverbs[i]} '
                                f'{new_adjectives[i]}')
            else:
                print("Not available, number of jokes more than number of available words")
                break
    return list_out


print(get_jokes_adv(2, repeat=True))
print(get_jokes_adv(4, repeat=False))
