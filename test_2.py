#	Список списков фильмов
#
# У Маши есть список ее любимых фильмов, но они хранятся в необычной структуре — списке списков, которые могут иметь
# произвольную вложенность.
# Она хочет преобразовать их в простой плоский список.
# Например, такой список
# ["a", ["b", "c", ["d"], "e"]]
# превратить в такой
# ["a", "b", "c", "d", "e"].
# Интерфейс списка списков на Java выглядит так:
# public interface NestedList {
#      // @return true если данный элемент содержит название фильма, а не список
#      public boolean isName();
#
#      // @return возвращает название фильма, если элемент содержит название, иначе null
#      public String getName();
#
#     // @return the nested list that this NestedInteger holds, if it holds a nested list
#      // Return null if this NestedInteger holds a single integer
#      public List getList();
#  }
#
# def func(_list, result=[]):
#     for i in _list:
#         if type(i) == list:
#             func(i)
#             #list(map(result.append, func(i)))
#         else:
#             result.append(i)
#     return result
#
# print(func(["a", ["b", "c", ["d"], "e"]]))



# def f[6,7]]],8]))unc(_list):
#     result=[]
#     for i in _list:
#         if type(i) == list:
#             result.extend(func(i))
#         else:
#             result.append(i)
#     return result
#
# print(func([7,[[[[2]]],[[[]],[4]],[4,5,[6,7]]],8]))

#
def merge(lst, res = []):
    for el in lst:
        merge(el) if isinstance(el, list) else res.append(el)
    return res

print(merge([7,[[[[2]]],[[[]],[4]],[4,5,[6,7]]],8]))