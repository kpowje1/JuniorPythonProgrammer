"""3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив
чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему
вы считаете, что функция соответствует заданным критериям."""


"""В данном случае используется так называемая сортировка слияния, в среднем время сортировки составляет O(n*log(n)).
Аналог такой сортировки является "Быстрая сортировка" у которой преимущество в экономии памяти, но есть исходы когда
сортировка будет составлять O(n^2) вместо O(n*log(n). Поэтому для этого задания остановился на сортировке слияния 
жертвуя памятью и выигрывая в скорости"""

import random

# Функция слияния списков
def merge(left_list, right_list):
    # Создание переменны для удобства и объявление пустого списка для слияния
    sort_list = list()
    left_list_range, right_list_range = len(left_list), len(right_list)

    i, j = 0, 0
    # Пока не подойдёт к последнему индексу левого или правого списка будем сравнивать элементы списков
    while i < left_list_range and j < right_list_range:
        if left_list[i] <= right_list[j]:
            sort_list.append(left_list[i])
            i += 1
        else:
            sort_list.append(right_list[j])
            j += 1
    # Добавляем к списку слияния оставшиеся элементы левого или правого списка (один из срезов будет пустой)
    sort_list += left_list[i:] + right_list[j:]
    return sort_list

# Основная функция с рекурсией разделения изначального списка на списки по одному элементу
def split_merge_sort(main_list):

    # Если список из одного элемента - то возвращаем его
    if len(main_list) <= 1:
        return main_list
    # Находим середину списка
    mid_list = len(main_list) // 2
    # Разделяем на левый и правый список и выполняем пока не дойдём до единичного элемента в списке
    left_list = split_merge_sort(main_list[:mid_list])
    right_list = split_merge_sort(main_list[mid_list:])

    return merge(left_list,right_list)


i = 0
random_list_of_nums = list()
while i < 7:
    random_list_of_nums.append(random.randint(1,1000))
    i+=1
print('Изначальный список: ' + str(random_list_of_nums))
random_list_of_nums = split_merge_sort(random_list_of_nums)
print('Отсортированный список: ' + str(random_list_of_nums))