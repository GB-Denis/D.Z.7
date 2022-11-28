# Задача 1 
# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if a ** 2 == b or b ** 2 == a:
#     print ('ДА')
# else:
#      print('НЕТ')        


# print ('Введите строку чисел')
# some_str = input().split(', ')
# a = int(some_str[0])
# b = int(some_str[1])
# if a ** 2 == b or b ** 2 == a:
#     print ('ДА')
# else:
#      print('НЕТ') 


# print ('Введите строку чисел')
# a, b = map(int, input().split(', '))
# if a ** 2 == b or b ** 2 == a:
#     print ('ДА')
# else:
#      print('НЕТ') 







# Задача 2
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# numbers = []
# for _ in range(5):
#     n = int(input())
#     numbers.append(n)
# max = numbers[0]
# for el in numbers:
#     if el > max:
#         max = el
# print(max)


# numbers = [0] * 5
# for index in range(5):
#     numbers[index] = int(input())
# max = numbers[0]
# for el in numbers:
#     if el > max:
#         max = el
# print(max)



# numbers = [0] * 5
# for index in range(5):
#     numbers[index] = int(input())
# print(max(numbers))    


# Самый оптимальный
# maxx = int(input())
# for _ in range(4):
#     n = int(input())
#     if n > maxx:
#         maxx = n
# print(maxx)  


# print(max(list(map(int, input().split(', ')))))




# Задача 3
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# 
# N = int(input('Введите число: '))
# if N > 0:
#     for s in range (-N, N):
#         print(s, end=', ')  
#     print(N)    
# else:
#     for s in range (-N, N, -1):
#         print(s, end=', ')  
#     print(N)    

# n = int(input())
# print(*list(range(-n, n + 1)), sep=', ')


# Задача 4
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.


# print(int(float(input())* 10%10))


# some_str = (input('Введите число: '))
# if ',' in some_str:
#     some_list = some_str.split(',')
#     print(some_list[1][0])
# else:
#     print('НЕТ')   
 

# some_str = (input('Введите число: '))
# if ',' in some_str:
#     ind = some_str.index(',')
#     print(some_str[ind + 1])
# else:
#     print('НЕТ') 


# number = float(input('Введите число '))
# if number % 1 != 0:
#     number = number * 10
#     number= int(number)
#     print(number % 10)
# else:
#     print('НЕТ')




# Задача 5
# Напишите программу которая на вход принимает число, и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# N = int(input('Введите число: '))
# if (N % 5 == 0 and N % 10 == 0 or N % 15 == 0) and N % 30 != 0:
#     print('ДА')
# else:
#     print('НЕТ')










