INPUT_FILE_NAME = "numbers.txt"
OUTPUT_FILE_NAME = "armstrong.txt"


def read_numbers():
    number_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as input_file:
            for number in input_file:
                number_list.append(number.strip())
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return number_list


def write_armstrong():
    number_list = read_numbers()
    armstrong_list = list()
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        for number in number_list:
            len_number = len(number)
            if len_number == 1:
                armstrong_list.append(number)
                continue
            armstrong_num = 0
            for num in number:
                try:
                    armstrong_num += int(num) ** len_number
                except ValueError as problem:
                    exit(f"We have a problem: {problem}")
            try:
                if armstrong_num == int(number):
                    armstrong_list.append(number)
            except ValueError as problem:
                exit(f"We have a problem: {problem}")
        for number in armstrong_list:
            output_file.write(f"{number}\n")


def main():
    read_numbers()
    write_armstrong()
    with open("armstrong.txt", "r") as input_file:
        print(input_file.read())


if __name__ == "__main__":
    main()
