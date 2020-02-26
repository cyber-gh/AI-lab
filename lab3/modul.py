a=10
def f():
    print("ceva")
    if __name__ == "__main__":
        print("din modul")
    else:
        print("din import")

if __name__ == '__main__':
    print("Bine ati venit in acest modul!")
    f()