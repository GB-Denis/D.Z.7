# # Задание 17. Задайте список из N элементов, заполненный числами из промежутка [-N,N].
# #  Найдите поизведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# import random
# n = int(input('Введите количество элементов: '))
# mult = 1
# some_list = [random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file.txt', 'w', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')
# with open('file.txt', 'r', encoding='utf-8') as file:
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print(mult)
