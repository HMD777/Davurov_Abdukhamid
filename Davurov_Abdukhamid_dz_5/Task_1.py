def odd_nums(number: int) -> int:
    for i in range(1, number+1, 2):
        yield i


n = 15
generator = odd_nums(n)

for _ in range(1, n + 1, 2):
    print(next(generator))
