from sys import argv


def multiply(*args):
    nr = 0
    for el in args:
        if el.isdigit():
            nr += int(el)
        else:
            return "Nu se poate"

    return nr


if __name__ == '__main__':
    print(multiply(*argv[1:]))