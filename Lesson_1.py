# Павел Грез  (Pavels Grjozs)
# Легкий уровень сложности (Easy)

# Задача 1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
print('Задача 1. Уровень: Легко.')

a = 1
b = 2.05
summ = a + b
message = ('В какую степень возведем сумму числел %d и %d равную %d :' % (a, b, summ))
power = input(message)
power = summ ** int(power)
print('Результат: %d ' % (power))

print('')

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
print('Задача 2. Уровень:  Легко.')

user_num = input('Введите число:')
user_num = int(user_num) + 2
print("Если к Вашему числу добавить 2 то получим %d " % (user_num))

print('')

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print('Задача 3. Уровень:  Легко.')

user_age = input('Введите Ваш возраст:')
if int(user_age) < 18 and int(user_age) > 0:
    print('Извините, пользование данным ресурсом только с 18 лет')
elif int(user_age) < 0:
    print('Похоже Вы еще не родились. Приходите попозже')
else:
    print('Злопожаловать на ресурс которым можно пользоваться с 18 лет')

print('')

# Нормальный уровень сложности (Normal)

# Задача 1: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
print('Задача 1. Уровень:  Нормально.')

user_num = input('Введите число для манипуляий: ')

while int(user_num) < 0 or int(user_num) > 10:
    user_num = input('Ваше число меньше 0 или больше 10. Заново введите число для манипуляий: ')
else:
    user_num = int(user_num) ** 2
    print('Вы ввели число удолетворающее заданию. Степень этого числа', user_num)

print('')

# Задача2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
print('Задача 2. Уровень:  Нормально.')

user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))

print('Число', user_num1, 'храниться в переменной user_num1')
print('Число', user_num2, 'храниться в переменной user_num2')

user_num1 = user_num1 + user_num2
user_num2 = user_num1 - user_num2
user_num1 = user_num1 - user_num2

print('После манипуляций')
print('Число', user_num1, 'храниться в переменной user_num1')
print('Число', user_num2, 'храниться в переменной user_num2')

print('')

