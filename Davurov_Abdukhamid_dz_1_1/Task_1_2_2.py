
number_min = 1
number_max = 1000
odd_list = []
odd_list_sqr = []
my_list = []
for i in range(number_min, number_max, 2):
    odd_list.append(i)
print(odd_list)
for i in odd_list:
    my_list.append((i ** 3)+17)
print(my_list)

def sum_list_1(dataset: list) -> int:
    new_list = []
    i = 0
    while i < len(dataset):
        n = int(dataset[i])
        nbr = 0
        while n > 0:
            digit = n % 10
            nbr = nbr + digit
            n = n // 10
        if nbr % 7 == 0:
            new_list.append(dataset[i])
        i += 1
    result= sum(new_list[0:len(new_list)])
    return result

result_1 = sum_list_1(my_list)
print(result_1)
