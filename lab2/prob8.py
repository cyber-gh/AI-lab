def filte1(target):
    return {x for x in target if str(x)[0] == str(x)[-1]}

def diagonal(mat):
    return {mat[i][j] for i in range(0, len(mat)) for j in range(0, len(mat[i])) if i == j}

if __name__ == '__main__':
    target = [232, 2332, 5, 11, 111, 123, 232]
    print(filte1(target))
    mat = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
    print(diagonal(mat))
    pass