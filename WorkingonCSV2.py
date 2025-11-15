with open("Industry.txt", "r") as file:
    lines = file.readlines()
    palindrome_count = 0
    for line in lines:
        words = line.split()
        for word in words:
            if word == word[::-1]:
                palindrome_count +=1

print("Number of palindrome words are: ", palindrome_count)
