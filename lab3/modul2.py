bording_char = " "


class ColumnDimError(Exception):
    pass


class ListArgumentError(Exception):
    pass


class GenericArgumentError(Exception):
    pass


def show_by_2(tuples, padding=8):
    if not type(tuples) is list:
        raise GenericArgumentError

    if any(not (type(el) is tuple) for el in tuples) or any(len(el) != 2 for el in tuples):
        raise ListArgumentError

    if any(max(map(lambda x: len(x), list(el))) > padding for el in tuples):
        raise ColumnDimError


    for el in tuples:
        for el in el:
            print(el + " " * (padding - len(el)), end=bording_char)
        print()


def show_by_3(tuples, bording_character=bording_char, padding=8):
    if not type(tuples) is list:
        raise GenericArgumentError

    if any(not (type(el) is tuple) for el in tuples) or any(len(el) != 3 for el in tuples):
        raise ListArgumentError

    if any(max(map(lambda x: len(x), list(el))) > padding for el in tuples):
        raise ColumnDimError

    for element in tuples:
        for el in element:
            print(" " * ((padding - len(el)) // 2) + el + " " * ((padding - len(el)) // 2), end=bording_character)
        print()


if __name__ == '__main__':
    pass
