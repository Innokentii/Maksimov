main_list = input('введите список чисел: ')
part_of_the_list = input('введите часть списка числа: ')

i = 0
x = list(main_list.split())
y = list(part_of_the_list.split())
while i < len(x):
    if x[i] == y[0] and x[i+1] == y[1]:
        print('да')
        break
    i += 1
    if i == len(x) - 1:
        print('нет')
        break


# введите список чисел: 1 2 3 4
# введите часть списка числа: 1 2
#
# да

# введите список чисел: 1 2 3 4
# введите часть списка числа: 2 4
#
# нет

