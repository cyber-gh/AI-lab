if __name__ == '__main__':
    with open("prob12.in", "r+") as fin:
        for line in fin.readlines():
            ans = eval(line[:-1])
            fin.write("=" + str(ans))
