import random

tries = 5
mn = 25
mx = 100  
target = random.randint(mn, mx)



while tries > 0:
    nr = int(input("nr="))

    if nr == target:
        print("ai ghicit")
        break
    if nr > target:
        print("prea mare")
    if nr < target:
        print("prea mic")
    tries -= 1

print("fail")