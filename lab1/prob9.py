from pprint import pprint

lst = ["papagal", "pisica", "soarece", "bolovan", "soparla", "catel", "pasare"]

first = [chr(x) for x in range(ord("a"), ord("z") + 1)]
mat = [[chr(x)] + 25 * [0] for x in range(ord("b"), ord("z") + 1)]
mat.insert(0, first)


def complete(mat, lst):
    for word in lst:
        for prev, next in zip(word, word[1:] + word[0]):
            mat[ord(prev) - ord("a") + 1][ord(next) - ord("a") + 1] += 1


def clear_empty(mat):
    mat = [line for line in mat if not all(el == 0 for el in line[1:])]
    to_remove = [j for j in range(0, len(mat[0])) if all(mat[i][j] == 0 for i in range(1, len(mat)))]
    mat = [[el for idx, el in enumerate(line) if idx not in to_remove] for line in mat]
    return mat


if __name__ == '__main__':
    complete(mat, lst)
    for line in clear_empty(mat):
        print(line)

    for i in range(1, len(mat)):
        for j in range(1, len(mat[i])):
            if mat[i][j] > 1:
                print("{} {}".format(i, j))
