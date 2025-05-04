# File Read & Write Challenge

def file_read_and_write():
    with open("input.txt", "r") as infile:
        content = infile.read()

    modified_content = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("Content modified and written to 'output.txt'.")

file_read_and_write()
