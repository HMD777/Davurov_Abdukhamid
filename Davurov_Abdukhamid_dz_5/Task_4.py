def get_numbers(src: list):
    src_res=[]
    for i in range(len(src)-1):
        if src[i] < src[i+1]:
            src_res.append(src[i+1])
    return src_res


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
