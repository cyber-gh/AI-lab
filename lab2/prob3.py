
def calculeaza1(union, intesection, difference):
    print(" A = ", union - difference)
    print(" B = ", intesection | difference)

def calculeaza2(intesection, a_b, b_a):
    print(" A = ", intesection | a_b)
    print(" B = ", intesection | b_a)

if __name__ == '__main__':
    calculeaza1({2, 3, 4, 5, 6}, {3}, {4, 5})
# 3, 4, 5 -- 2, 3, 6