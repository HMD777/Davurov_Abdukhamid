task = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(task)
task_new = []
task_nbr=0

for i in task:

    if not i.isalpha():
        task_new.append('"')
        task_new.append(i)
        task_new.append('"')

    else:
        task_new.append(i)


print(task_new)
