# 1.Задача на проверку простоты числа
'''
def is_prime(a):

    if a == 1:
        return False

    if a == 2 or a % 2 != 0:
        for i in range(3, int(a ** 0.5), 2):
            if a % i == 0:
                return False
        return True
    return False

a_ = int(input('Введите число: '))
print(is_prime(a_))
'''

# 2. Задача о сортировке массива
'''
def sort_array(array_):

    for i in range(0, len(array_)):
        for i in range(0, len(array_) - 1):
            if array_[i] > array_[i + 1]:
                array_[i], array_[i + 1] = array_[i + 1], array_[i]
    return array_

array = []
array_size = int(input('Введите количество элементов массива: '))

for i in range(0, array_size):
    array.append(int(input('Введите число для элемента массива ' + str(i)+': ')))

print(sort_array(array))
'''

# 3. Задача о поиске наибольшего элемента в массиве
'''
def max_value_array(array):
    array_max = 0

    for i in range(0, len(array)):
        if array[i] > array_max:
            array_max = array[i]

    return 'Наибольшее число: ' + str(array_max)

array = []
array_size = int(input('Введите количество элементов массива: '))

for i in range(0, array_size):
    array.append(int(input('Введите число для элемента массива ' + str(i)+': ')))

print(max_value_array(array))
'''

# Задача о вычислении числа Фибоначчи
'''
n = int(input('Введите число: '))
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
'''

# Задача на хэш-таблицы
'''
def repeat_words(array_):
    repeat_words = []

    for i in range(0, array_size):
        repeat_words.append(0)

    for i in range(0, len(array_)):
        for j in range(0, len(array_)):
            if array_[i] == array_[j]:
                repeat_words[i] += 1

    index_repeat_word = -1

    for i in range(0, len(array_)):
        if repeat_words[i] > index_repeat_word:
            index_repeat_word = i

    if index_repeat_word == -1:
        return 'Строки не повторяются'
    else:
        return index_repeat_word

array = []
array_size = int(input('Введите количество элементов массива: '))

for i in range(0, array_size):
    array.append(input('Введите строку для элемента массива ' + str(i)+': '))

print(array[repeat_words(array)])
'''




