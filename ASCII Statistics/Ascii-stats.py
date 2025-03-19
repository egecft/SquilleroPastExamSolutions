INPUT_FILE_NAME = "landscape.txt"
# INPUT_FILE_NAME = "landscape2.txt


def read_file():
    line_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip("\n")
                line_list.append(clean_line)
    except OSError as problem:
        print(f"We have a problem: {problem}")
    print(line_list)
    return line_list


def get_input():
    x = int()
    y = int()
    size = int()
    try:
        cord_input = input("Please, enter the coordinates (x,y): ")
        x, y = cord_input.strip().split(",")
        x = int(x.strip())
        y = int(y.strip())
        size_input = input("Please, enter the square size: ")
        size = int(size_input.strip())
    except ValueError as problem:
        exit(f"We have a problem: {problem}")
    return x, y, size


def main():
    read_file()
    get_input()
    pass


if __name__ == "__main__":
    main()
