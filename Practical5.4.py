with open("Industry.txt", "rb") as file:

    first_byte = file.read(10)
    print("First 10 bytes of the file are: ", first_byte)

    position = file.tell()
    print("current file pointer position is: ", position)

    file.seek(0)
    print("Pointer moved to start: ", file.tell())

    next_byte = file.read(5)
    print("Next 5 bytes are: ", next_byte)

    file.seek(-3,2)
    last_bytes = file.read()
    print("Last 3 bytes: ", last_bytes)