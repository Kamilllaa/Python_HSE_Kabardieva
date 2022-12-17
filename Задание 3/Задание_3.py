# acomprehension, filter, map

string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"


#1. Найти все числа от 1 до 1000, которые делятся на 17

def task1():
    return [x for x in range(1, 1001) if x % 17 == 0]


#2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2

def task2():
    return [n for n in range(1, 1001) if '2' in str(n)]


#3. Найти все числа от 1 до 10000, которые являются палиндромом

def task3():
    return list(filter(lambda i: (i == "".join(reversed(i)) and len(i) > 1), [str(x) for x in range(1, 10001)]))


#4. Посчитать количество пробелов в строке

def task4(string):
    return len(list(filter(lambda i: (i == " "), string)))


#5. Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова

def task5(string):
    return "".join([i for i in string if i not in 'euioaEUIOA'])


#6. На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5

def task6(string):
    return list(filter(lambda i: (len(i) < 5), string.split()))

#7. На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.

def task7(string):
    return {x: len(x) for x in string.split()}


#8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.

def task8(string):
    return {x: string.count(x) for x in string if x != ' ' and ':'}


#9. На входе список чисел, получить список квадратов этих чисел / use map

def task9():
    return list(map(lambda x: x ** 2, [x for x in range(1, 15)]))


#10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2.
# На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)

coordinates = [(1, 1), (2, 3), (5, 3), (1, 3)]

def task10():
    return {(x, y): ((x ** 2 + y ** 2) ** (0.5)) for x, y in coordinates if y == 5 * x - 2}

#11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.

def task11():
    return [n ** 2 for n in range(2, 28) if n % 2 == 0]


#12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти

def task12(coordinates):
    return max([(x ** 2 + y ** 2) ** 0.5 for x, y in coordinates if x >= 0 and y >= 0])


#13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]

nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]

def task13(nums_first, nums_second):
    return [[(x + y, x - y)] for x, y in zip(nums_first, nums_second)]


#14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.

digits = ['43141', '32441', '431', '4154', '43121']

def task14(digits):
    return list(filter(lambda i: ((int(i) ** 2) % 2 == 0), digits))


#15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

#Мы хотим получить нормальную таблицу, чтобы импортировать в csv

"""
[
  {
    'name': 'Petya',
    'grade': '5'
    'subject': 'math'
    'year': '1999'
  },
  {
    'name': 'Vasya',
    'grade': '5'
    'subject': 'language'
    'year': '2000'
  },
  ...
]

"""

def task15(input_str):
    return [dict(zip(list(zip(*[title.split(',') for title in input_str.split('\n')]))[0], value))
            for value in list(zip(*[value.split(',') for value in input_str.split('\n')]))[1:]]


#16. Получить сумму по столбцам у двумерного списка

a = [[11.9, 12.2, 12.9],
     [15.3, 15.1, 15.1],
     [16.3, 16.5, 16.5],
     [17.7, 17.5, 18.1]]

result = [61.2, 61.3, 62.6]

def task16(a):
    return (list(map(sum, zip(*a))))
