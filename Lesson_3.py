# Задание - 1

# Павел Грез  (Pavels Grjozs)
# Легкий уровень сложности (Easy)

# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def task_1(name, age, city):
    return print('{}, {} год(а), проживает в городе {}'.format(name, age, city))


name = input('Введите Ваше Имя:')
age = int(input('Введите Ваш возраст:'))
city = input('Введите Ваш город проживания:')

task_1(name, age, city)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def task_2(number_1, number_2, number_3):
    max_number = [number_1, number_2, number_3]
    return print(max(max_number))


number_1 = int(input('Введите чило 1: '))
number_2 = int(input('Введите чило 2: '))
number_3 = int(input('Введите чило 3: '))

task_2(number_1, number_2, number_3)



# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов







#Normal 
# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

#Данные
names = ['Alex', 'Igor', 'Alice', 'Petja', 'Aleksandrs', 'John', 'Аль Капоныч']
salary = ['1000', '5000', '10000', '900', '11000', '0', '99999']

#Создаем словарь
data_base = dict(zip(names, salary))
#Проверка
# print(data_base)

#key employee_name + значение ключа data_base[employee_name]
# Пишем в файл
file = open('salary.txt', "w", encoding='utf-8')
for employee_name in data_base:
    file.write(employee_name + ' - ' + data_base[employee_name] + '\n')
file.close()

# Читаем из файла
salary_file = open('salary.txt', encoding='utf-8')
my_file = salary_file.read()
print(type(my_file))
print(my_file)
file.close()


#Как прочитать эллемент при этом понимая где зарплата а где имя ... в процессе.

