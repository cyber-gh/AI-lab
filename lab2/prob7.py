def int_and_divides(lst, n):
    return all(int(x) == x and x % n == 0 for x in lst)

def is_all_digit(lists):
    return any(all(str(x).isdigit() for x in lst) for lst in lists)

def has_one_all_zero(mat):
    return any(all(x == 0 for x in line) for line in mat)

def contains_all(target, words):
    return all(word in target for word in words)

if __name__ == '__main__':
    lst = [2, 8, 10]
    print(int_and_divides(lst, 2))