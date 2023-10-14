list1 = list('曾许人间第一流')
list2 = []
for i in list1:
    list2 += i
    list2.extend([i])
print(list2)
print(list2, end='')  #  end换行end=''换行变成换空格
for i in range(1,10):
    print(i)
