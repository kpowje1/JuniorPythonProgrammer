"""
2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.
"""
from collections import deque

"""Плюсы данной реализации:
- Легка в написании,
- Явно читаема, нет отдельной библиотеки и используются методы проходимые в начале обучения;

Минусы данной реализации:
В отличие от доступных библиотек скорость выполнения функций внутри класса более длительная, список один из самых 
медленных типов данных при работе с добавлением/удалением/чтением данных из него (чтение/удаление O(n))"""
class CircleListFIFO():
    def __init__(self):
        self.list = list()

    def pop(self):
        if len(self.list) > 0:
            return print('Элемент ' + self.list.pop(0) + ' удалён из очереди')
        else:
            return print('Очередь пуста')

    def add(self, value):
        self.list.append(value)
        return print('Элемент ' + value + ' добавлен в конец очереди')

    def out(self):
        return print(self.list)


"""Плюсы:
- Высокая скорость выполнения функций описанных в классе (добавление и извлечение элементов с любой стороны O(1)),
- Более широкий выбор методов при работе с очередью;
"""
class CircleDequeFIFO():
    def __init__(self):
        self.queue = deque()

    def add(self, value):
        self.queue.append(value)
        return print('Элемент ' + value + ' добавлен в конец очереди')

    def pop(self):
        if len(self.queue) > 0:
            return print('Элемент ' + self.queue.popleft() + ' удалён из очереди')
        else:
            return print('Очередь пуста')

    def out(self):
        return print(self.queue)

# Пример работы первого класса CircleListFIFO
a = CircleListFIFO()
print('Пример работы первого класса CircleListFIFO: ')
a.pop()
a.add('test1')
a.add('test2')
a.out()
a.pop()
a.out()
print('\n')

# Пример работы второго класса CircleDequeFIFO
b = CircleDequeFIFO()
print('Пример работы второго класса CircleDequeFIFO: ')
b.pop()
b.add('test3')
b.add('test4')
b.out()
b.pop()
b.out()