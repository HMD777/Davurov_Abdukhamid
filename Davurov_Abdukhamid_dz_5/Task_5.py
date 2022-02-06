def get_uniq_numbers(src: list):
    uniq_nbrs = set()
    temp_nbrs = set()
    for i in src:
        if i not in temp_nbrs:
            uniq_nbrs.add(i)
        else:
            uniq_nbrs.discard(i)
        temp_nbrs.add(i)
    uniq_nbrs_ord = [i for i in src if i in uniq_nbrs]
    return uniq_nbrs_ord


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
