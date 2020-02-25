

if __name__ == '__main__':
    try:
        with open("mat.in") as fin:
            matrix = list(map(lambda x: x[:-1].split(" "), fin.readlines()))
            print(matrix)
            check = set([len(x) for x in matrix])
            if len(check) > 1:
                raise ValueError
            anotherCheck = [1 if x.isdigit() else 0 for y in matrix for x in y]
            if sum(anotherCheck) != len(anotherCheck):
                raise Exception
            print(anotherCheck)
    except FileNotFoundError:
        print("file not found")
    except ValueError:
        print("wrong format of liens")
    except Exception:
        print("value error")


