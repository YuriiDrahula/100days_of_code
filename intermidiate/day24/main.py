# The way how to read a file
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# The second way how to read a file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Change all text in the file to your text
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Append new text to the current file
with open("my_file.txt", mode="w") as file:
    file.write("\nNew text.")