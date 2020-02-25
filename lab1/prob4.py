def shiftLeft(arr):
    return arr[1:] + arr[0]

def shiftRight(arr):
    return arr[-1] + arr[:-1]

lst = str(input("input="))
for el in range(0, len(lst)):
    print(lst)
    lst = shiftLeft(lst)

print("\n")

for el in range(0, len(lst)):
    print(lst)
    lst = shiftRight(lst)

print()
while len(lst) > 1:
    print(lst[0] + lst[-1])
    lst = lst[1:-1]