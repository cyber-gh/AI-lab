if __name__ == '__main__':

    log = open("logs.txt", "w")
    idx = 0
    while True:
        command = input("comanda=")
        if command == "scriere_continut":
            idx = 1
            with open("result_{}.out".format(idx), "w") as fout, open("input.in", "r") as fin:
                for line in fin.readlines():
                    fout.write(line)
        if "scrie_cuvinte" in command:
            idx = 2
            with open("input.in") as fin, open("result_{}.out".format(idx), "w") as fout:
                sort_criteria = command.split(" ")[1]
                words = []
                for line in fin.readlines():
                    words += [x for x in line.split(" ")]
                if sort_criteria == "asc":
                    words = sorted(words, reverse=False)
                if sort_criteria == "desc":
                    words = sorted(words, reverse=True)
                for word in words:
                    fout.write(word + "\n")
        if "scrie_linii" in command:
            idx = 3
            start, finish = tuple(command.split(" ")[1].split("-"))
            start = int(start)
            finish = int(finish)
            with open("input.in") as fin, open("result_{}.out".format(idx), "w") as fout:
                for index, line in enumerate(fin.readlines()):
                    if start <= index + 1 <= finish:
                        fout.write(line)

        if command == "iesire":
            break
