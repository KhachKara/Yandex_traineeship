# Название фильма
# Маша хочет иметь возможность "испортить" название фильма. Она придумала такой алгоритм. Все буквы в названии
# фильма надо отсортировать по частоте их встречаемости (начиная с самых частых).
# Например, название "Arrival" превратится в "rrAival" (возможно и "rrlAiva", и другие варианты), потому что буква "r"
# встречается два раза, а остальные один раз.
# Реализуйте для Маши этот алгоритм на любом языке программирования.
# Пример заголовка метода на Java:
# public String scramble(String name)


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
j = 1
result = []
name = list('Arrival')
for el in name:
    num = count_char(name, el)

    if num > j:
        j = num
        result.append(el)
    # print('{} - {}'.format(el, num))
