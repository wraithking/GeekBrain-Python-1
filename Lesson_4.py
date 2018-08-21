# Павел Грез  (Pavels Grjozs)
# Легкий уровень сложности (Easy)

# Библиотеки для всех задач
import random
import math

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# Создаю первый список и заполняю его произвольными целыми числами.
# Создаю второй список и заполняю его квадратами первого списка.
print('Задача 1. Уровень: Легко.')

generated_list = [random.randint(1, 10) for list_element in range(4)]
generated_list_sqr = [el ** 2 for el in generated_list]
print(generated_list, '-->', generated_list_sqr)

print('\n')
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print('Задача 2. Уровень: Легко.')

# Создаю список с фруктами.
fruits_list_base = ['Гранат', 'Грейпфрут', 'Грумичама', 'Груша', 'Гуайява земляничная', \
                    'Гуайява коста-риканская', 'Гуайява красная', 'Гуайява обыкновенная', \
                    'Гуарана', 'Давидсония', 'Дамские пальчики', 'Деревянное яблоко', 'Десертный квандонг', \
                    'Джекфрут', 'Древесная калебаса', 'Дуку', 'Дуриан']

# Для практики - списки с фруктами будет создавать случайные, что бы было интеерсно а не заданные.

fruits_list_one = generated_list = [random.randint(0, 16) for list_element in range(8)]

fruits_list_two = generated_list = [random.randint(0, 16) for list_element in range(8)]

# Задаю значения спискам.
list_frut_1 = [fruits_list_base[fruits_list_one] for fruits_list_one in fruits_list_one]
list_frut_2 = [fruits_list_base[fruits_list_two] for fruits_list_two in fruits_list_two]

print('Первый список:', list_frut_1)
print('Второй список:', list_frut_2)

# Создаю переменные для работы цикла сравнения списков.
list_frut_3 = []
i = 0
j = 0

for fruts in list_frut_1:
    if list_frut_1[i] == list_frut_2[j]:
        list_frut_3.append(list_frut_1[i])
        i += 1
    j += 1

if not list_frut_3:
    print('Нет общих эллементов')
else:
    print('Фрукты совпали в обоих списках', list_frut_3)

print('\n')
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print('Задача 3. Уровень: Легко.')

random_list_one = generated_list = [random.randint(-100, 100) for list_element in range(10)]
print('Список:', random_list_one)

only_positive = [el for el in random_list_one if el > 0 and el % 3 == 0 and el % 4 != 0]

if not only_positive:
    print('Нет таких чисел в списке:', random_list_one)
else:
    print('Есть требуемые числа в списке:', random_list_one, 'это', only_positive)
