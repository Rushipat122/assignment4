try:
    with open("sample.txt", "rt") as fh:
        l1 = fh.readline()
        l2 = fh.readline()

        print(f"line 1: {l1}")
        print(f"line 2: {l2}")
except FileNotFoundError:
    print("the file \"sample.txt\" not found")