def generate_matrix(n):
    return [[x] * n for x in range(1, n + 1)]


def flavius(mat, k):
    return {mat[i][j] for i in range(k, len(mat)) for j in range(k, len(mat))}


def filter_odd(mat):
    return [[x for idx, x in enumerate(line) if (idx + 1) % 2 == 1] for line in mat]


def filter_by_ison(mat, ison):
    return [[mat[i][j] if ison[i][j] else 0 for j in range(0, len(mat[i]))] for i in range(0, len(mat))]


def generate_diagonal(n, element):
    return [[element if i == n - j - 1 else 0 for j in range(0, n)] for i in range(0, n)]

def combine_lists(lst1, lst2):
    return [[el1 if el1 > el2 else el2 for el1 in lst1] for el2 in lst2 ]

if __name__ == '__main__':
    mat = generate_matrix(5)
    is_on = [[1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0]]
    print(mat)
    print(flavius(mat, 2))
    print(filter_odd(mat))
    print(filter_by_ison(mat, is_on))
    print(generate_diagonal(5, 3))

    lst1 = [1, 5, 2, 4]
    lst2 = [3, 7, 8, -1]
    print(combine_lists(lst1, lst2))
