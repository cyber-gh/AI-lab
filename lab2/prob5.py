from string import ascii_lowercase

def gen1(n):
    return [x * ((-1) ** x) for x in range(0, n + 1)]

def odd(lst):
    return [x for x in lst if x % 2 == 1]

def oddIdx(lst):
    return [x for idx, x in enumerate(lst) if idx % 2 == 1]

def sameParity(lst):
    return [x for idx, x in enumerate(lst) if idx % 2 == x % 2]

def neighbors(lst):
    return list(zip(lst, lst[1:] + [lst[0]]))

def mul_table(n):
    return [ [ "{} * {} = {}".format(x, y, x * y) for y in range(1, n) ] for x in range(1, n + 1) ]

def rotate_left(target):
    test_list = list(target)
    return [ [test_list[(i + offset) % len(test_list)] for i, x in enumerate(test_list)] for offset in range(0, len(target)) ]


def traingel(n):
    return [ [ y for x in range(0, y)] for y in range(0, n)]
if __name__ == '__main__':
    print([ x for x in range(0, 11) if x % 2 == 1])
    print(list(ascii_lowercase))
    print(gen1(20))
    print(odd([1, 2, 3, 4, 5]))
    print(oddIdx([1, 2, 3, 4, 5]))
    print(sameParity([0, 1, 2, 3, 4, 5]))
    print(neighbors([1, 2, 3]))
    print(mul_table(9))
    print(rotate_left("abcde"))
    print(traingel(5))
