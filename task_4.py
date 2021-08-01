# coding=utf-8
input = input('Для вычисления суммы чисел от 1 до n, введите n ')


def f(num):
    if num < 1:
        print('Введите число большее либо равное 1')
        return -1
    elif num == 1:
        return 1
    else:
        if num >= 1:
            return f(num - 1) + num


print(f(input))

