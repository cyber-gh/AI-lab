lst = ["margareta", "crizantema","lalea"," zorea , violeta, orhidee","trandafir","gerbera , iasomie","iris","crin "]

toAdd = input("new=")
if toAdd in lst:
    idx = lst.index(toAdd)
    lst = lst[:idx] + lst[idx + 1:]
lst.append(toAdd)
print(lst)


extended = [x for x in lst if len(x.split(",")) > 1]
lst = [x for x in lst if not(x in extended)]
for ext in extended:
    lst += ext.split(",")

def selectByChar(target, c):
    return list(filter(lambda x: c in x, target))

print(lst)

print(selectByChar(lst, "o"))

alfabetical = sorted(lst, reverse = False)
nonalfabetical = sorted(lst, reverse = True)

print(alfabetical)
print(nonalfabetical)