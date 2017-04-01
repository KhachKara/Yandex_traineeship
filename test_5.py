# Задача на нахождения факториала


def fact_k(num):
    result = 1
    if num < 0:
        return -1
    elif num == 0:
        return 1
    else:
        for i in range(num):
            result *= (i + 1)
    return result
print(fact_k(5))


def fact_m(num):
    result = 1
    for i in range(1, num + 1):
        result *= (i)
    return result
print(fact_m(5))


def fackt_rek(num):
    if num < 0:
        return -1
    if num <= 1:
        return 1
    print(num)
    return fackt_rek(num - 1) * num
print(fackt_rek(5))
