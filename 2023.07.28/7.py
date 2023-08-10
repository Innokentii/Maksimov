list_of_dicts = [
    {
        'Барнаул': 4,
        'Владивосток': 3,
        'Волгоград': 2,
        'Нижний Новгород': 8,
        'Санкт-Петербург': 4,
        'Ульяновск': 8,
        'Уфа': 7,
        'Хабаровск': 2,
        'Ярославль': 1
    },
    {
        'Владивосток': 3,
        'Воронеж': 4,
        'Казань': 2,
        'Москва': 8,
        'Новокузнецк': 3,
        'Новосибирск': 4,
        'Омск': 1,
        'Пермь': 2,
        'Тольятти': 1,
        'Уфа': 3
    },
    {
        'Барнаул': 1,
        'Владивосток': 1,
        'Волгоград': 9,
        'Москва': 1,
        'Новосибирск': 6,
        'Санкт-Петербург': 3,
        'Ульяновск': 9
    },
    {
        'Владивосток': 1,
        'Воронеж': 3,
        'Екатеринбург': 6,
        'Оренбург': 3,
        'Санкт-Петербург': 8,
        'Тольятти': 2
    }
]
plenty = set()
for i in range(len(list_of_dicts)):
    plenty = plenty | set(list_of_dicts[i])
plenty_key = dict.fromkeys(sorted(plenty, reverse = False), set())

for list_ in list_of_dicts:
    for key, val in plenty_key.items():
        try:
            if list_[key]:
                try:
                    plenty_key[key] = plenty_key[key] | {str(list_[key])}
                    #print(plenty_key[key])
                except KeyError:
                    plenty_key[key]
        except KeyError:
            plenty_key[key]
            
for k, v in plenty_key.items():
    print(f'{k}: {v}')

# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 7.py
# Барнаул: {'1', '4'}
# Владивосток: {'3', '1'}
# Волгоград: {'2', '9'}
# Воронеж: {'3', '4'}
# Екатеринбург: {'6'}
# Казань: {'2'}
# Москва: {'8', '1'}
# Нижний Новгород: {'8'}
# Новокузнецк: {'3'}
# Новосибирск: {'6', '4'}
# Омск: {'1'}
# Оренбург: {'3'}
# Пермь: {'2'}
# Санкт-Петербург: {'8', '3', '4'}
# Тольятти: {'1', '2'}
# Ульяновск: {'8', '9'}
# Уфа: {'3', '7'}
# Хабаровск: {'2'}
# Ярославль: {'1'}
# >>>