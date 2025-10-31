with open("output.txt", "a+") as fh:
    imp1 = input("enter text to write to the file: ")
    fh.write(imp1+ "\n")
    print("data is successfully added to output.text")

    imp2 = input("enter text to append: ")
    fh.write(imp2+ "\n")
    print("data is successfully appended")
    fh.seek(0)
    print("final output of output.txt is:")
    content = fh.read()
    print(content)
