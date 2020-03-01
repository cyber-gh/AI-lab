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
            with open("input.in") as fin:
                sort_criteria = list(command.split(" ")[1])
                if sort_criteria == "ord":
                    for line in fin.readlines():
