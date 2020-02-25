dct = {((1, 4), "mic"), ((4, 8), "mediu"), ((8, 15), "mare")}
dct = dict(dct)
lst = ["bau-bau", "bobocel", "14 pisici", "1pitic", "pisicel", "botosel", "414", "ham", "-hau", "bob", "bocceluta"]
if __name__ == '__main__':
    for (mn, mx), value in dct.items():
        print(mn, mx, value)

    ans = dict()
    for char in set("".join(lst)):
        ans[char] = [word for word in lst if char in word]

    print(len(ans.keys()))
    for char in set(x for x in "".join(lst) if x.isalpha() == False and x.isnumeric() == False):
        del ans[char]
    print(ans)

    print(len(ans.keys()))

    for key, value in ans.items():
        for word in value:
            for (mn, mx), value in dct.items():
                if mn < len(word) < mx:
                    print(dct[(mn, mx)], end=" ")
        print()
