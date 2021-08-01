# coding=utf-8
left_list_input = input('Введите первый список ')
right_list_input = input('Введите второй список ')

def f(list_1, list_2):
    left_side_counted = len(list_1)
    right_side_counted = len(list_2)

    if left_side_counted == right_side_counted:
        total = []
        for i in range(0, left_side_counted):
            total.append(left_list_input[i] * right_list_input[i])
        return total
    else:
        return []


print(f(left_list_input, right_list_input))
