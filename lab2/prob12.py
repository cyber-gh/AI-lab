if __name__ == '__main__':
    output = []
    with open("prob12.in", "r+") as fin:
        for line in fin.readlines():
            ans = eval(line[:-1])
            output.append("{}={}".format(line[:-1], ans))

    with open("prob12.in", "w+") as fout:
        for line in output:
            fout.write(line + "\n")
