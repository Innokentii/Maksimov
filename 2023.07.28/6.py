binary_number = input('введите двоичное число: ')
prefix = {'b', '1', '0'}
x = list(binary_number)

is_prefix_chars = [{str(n)} < prefix for n in x]
while True:
    for i in range(len(x)):
        if is_prefix_chars[i-1] == False:
            print(f'\n{"нет"}\n')
            break
    if (
            str(x[0]) == '0' and str(x[1]) == 'b'
         or str(x[0]) == 'b' and str(x[1]) != 'b'
         or str(x[0]) != '1' and str(x[1]) == 'b'
         or str(x[0]) != 'b' and str(x[1]) != 'b'
    ):
        print(f'\n{"да"}\n')
    else:
        print(f'\n{"нет"}\n')
    break


# введите двоичное число: 0101
#
# да

# введите двоичное число: b11
#
# да

# введите двоичное число: 0b11001
#
# да

# введите двоичное число: 1b0101
#
# нет

