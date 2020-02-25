def sortAsStr(lst):
    lst.sort(key=lambda x: str(x))
    print(lst)


def sort2(lst):
    lst.sort(key=lambda x: str(x)[::-1])
    print(lst)


def sort3(lst):
    lst.sort(key=lambda x: len(str(x)))
    print(lst)

def sort4(lst):
    lst.sort(key=lambda x: eval(x))
    print(lst)

if __name__ == '__main__':
    lst = [123, 3, 21, 32]
    sortAsStr(lst)
    sort2(lst)
    sort3(lst)

    special = ["1+2+3", "2-5", "3+4", "5*10"]
    sort4(special)
