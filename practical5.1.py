with open("Industry.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = 0
    char_count = 0
    for line in lines:
        word = line.split()
        word_count += len(word)
        char_count += len(line)

print("Number of lines: ", line_count)
print("Number of words: ", word_count)
print("Number of characters: ", char_count)
  

