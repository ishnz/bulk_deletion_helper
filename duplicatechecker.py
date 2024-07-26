def open_file():
    file = input("Enter the file name: ")
    try:
        with open(file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    file = open_file()
    if file is None:
        return
    arr = [ '' ]
    for line in file.split("\n"):
        for i in arr:
            if i == line:
                print("Duplicate found: " + i)
        arr.append(line)

if __name__ == "__main__":
    main()
