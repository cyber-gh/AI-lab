from string import ascii_lowercase


# 1

def is_same(lst):
    return len(set(lst)) == 1

# 2
def is_alphabet(target):
    target = str(target)
    return len(set(map(lambda x: 1 if x in target else 0, ascii_lowercase))) == 1

# 3
def is_anagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))

# 4 pe numere binare, skipped

# 5
def cartesian_product(lst1, lst2):
    return [[x, y] for x in lst1 for y in lst2]

if __name__ == '__main__':
    print(is_same([1, 1, 1]))
    print(is_alphabet("abcdefghijklmnopqrstuvyz"))
    print(is_alphabet("abcdefghijklmnopqrstuvwxyz"))
    print(is_anagram("123", "321"))
    print(is_anagram("123", "351"))
    print(cartesian_product([1, 2], [3, 4, 5]))
