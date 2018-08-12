# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


print('Задача 1. Уровень: Легко.')

fruits_list = ["яблоко", "банан", "киви", "арбуз"]
i = 1
for fruits in fruits_list:
    print('{}. {}'.format(i, fruits))
    i += 1

print('')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('Задача 2. Уровень: Легко.')

list_1 = ["Tom", "Sam", "Bob", "Bill", "Alice", "Sam", "Bob", "Don Carleone", "Tom"]
list_2 = ["Tom", "Sam", "Bob"]

variable_of_list_1 = 0
variable_of_list_2 = 0

len_of_list_1 = len(list_1)
len_of_list_2 = len(list_2)

while variable_of_list_2 < len(list_2):
    while variable_of_list_1 < len(list_1):
        if list_1[variable_of_list_1] == list_2[variable_of_list_2]:
            print(list_1[variable_of_list_1])
        variable_of_list_1 += 1
    else:
     variable_of_list_2 += 1

print(list_1)
print(list_2)




print('')


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
