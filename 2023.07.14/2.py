import sys

std = sys.stdin.readlines()
num_2_1 = int(std[0])
num_2_2 = int(std[1])
# УДАЛИТЬ: неиспользуемая переменная
num_2_0 = 0

# ИСПРАВИТЬ: приоритет любого математического оператора выше, чем любого оператора сравнения — скобки избыточны
if (num_2_1 % num_2_2) == 0:
    # ИСПРАВИТЬ: ни с функцией print() не разобрались, ни f-строки не используете — а это два из трёх основных средств генерации строк — срочно исправляйтесь (начать можно с моих лекций, как ни странно)
    print(num_2_1, ' делится на ', num_2_2, ' нацело',
          # ИСПРАВИТЬ: используйте оператор целочисленного деления
          '\nчастное: ', (num_2_1 / num_2_2))
else:
    print(num_2_1, ' НЕ делится на ', num_2_2, ' нацело',
          '\nнеполное частное: ', int(num_2_1 / num_2_2), '\nостаток: ',
          # ИСПРАВИТЬ: это не остаток от деления, а вещественное число — остаток от деления у вас уже вычислен ранее, используйте его
          float(num_2_1 / num_2_2) - int(num_2_1 / num_2_2))

# СДЕЛАТЬ: лучше выстроить код так, чтобы не прописывать генерацию очень похожего литерала второй раз, не использовать блок else, а функцию print() вызывать только один раз — подумайте, как это можно сделать


# 6
# 2
# ^Z
# 6  делится на  2  нацело
# частное:  3.0

# 5
# 2
# ^Z
# 5  НЕ делится на  2  нацело
# неполное частное:  2
# остаток:  0.5


# ИТОГ: нужно лучше — 2/4
