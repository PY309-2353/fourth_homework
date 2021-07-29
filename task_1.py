string_input = input('Что умножаем? ')
int_input = int(input('На сколько? '))

def f(to_multiply, quantity):
    print(to_multiply * quantity)

f(string_input, int_input)