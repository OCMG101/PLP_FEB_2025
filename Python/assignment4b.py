# Error Handling Lab

def safe_file_reader():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Contents:")
            print(content)
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")

safe_file_reader()
