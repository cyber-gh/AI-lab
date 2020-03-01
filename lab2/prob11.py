if __name__ == '__main__':
    lst = list()
    with open("prob11.in", "r") as fin:
        for line in fin.readlines():
            (idx, nume) = tuple(line[:-1].split(":"))
            idx = int(idx)
            if idx > len(lst):
                lst = lst + (["gol"] * (idx - len(lst) - 1))
                lst.append(nume)
            else:
                lst[idx] = nume

    print(lst)
