left_part_input = input('Где смотрим? ')
right_part_input = input('Что ищем? ')

def f(where, what):
    count = 0
    letter_list = [x for x in where]
    for letter in letter_list:
        if letter == what:
            count += 1
    return count

print(f(left_part_input, right_part_input))