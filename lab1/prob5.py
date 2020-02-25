lst = ["haha", "poc", "Poc", "POC", "haHA", "hei", "hey", "HahA", "poc", "Hei"]
freq = {}

for el in lst:
    s = el.lower()
    if s in freq:
        freq[s] = int(freq[s]) + 1
    else:
        freq[s] = 1


for key, value in freq.items():
    print("{} apare de {} ori".format(key, value))