with open("Industry.txt", "r") as file:
    lines = file.readlines()

with open("Even.txt", "w") as even_file,\
open("Odd.txt", "w") as odd_file:
    for i in range(len(lines)):
        if(i+1)%2 == 0:
            even_file.write(lines[i])
        else:
            odd_file.write(lines[i])

print("Even and odd files are successfully created")
