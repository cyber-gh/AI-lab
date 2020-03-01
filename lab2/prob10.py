
def generate1(k):
    return { i : [x for x in range(1, i)] for i in range(1, k, 2)}

def generate2(target):
    return { c : [word for word in target if c in word] for c in set("".join(target))}

def generate3(target):
    return { key: [x for x in range(key[0], key[1])] for key in target}

if __name__ == '__main__':
    print(generate1(10))
    target = ["test", "saf", "cheaper", "big", "small"]
    print(generate2(target))

    target2 = [(2, 6), (5, 10), (8, 12)]
    print(generate3(target2))