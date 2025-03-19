INPUT_FILE_NAME = "parole_italiane.txt"
# Input "names.txt" as the file containing the names


def read_file():
    word_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip()
                word_list.append(clean_line)
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return word_list


def get_file_input():
    file_name = input("Please, introduce the name of the file with the names: ")
    return file_name


def read_file_input(file_name):
    name_list = list()
    try:
        with open(file_name, "r") as file:
            for line in file:
                clean_line = line.strip()
                name_list.append(clean_line)
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return name_list


def main():
    word_list = read_file()
    file_name = get_file_input()
    name_list = read_file_input(file_name)

    for name in name_list:
        output_words = list()
        lower_name = name.lower()
        print(f"Name: {name}")

        for word in word_list:
            letter_diff = 0
            if not len(word) == len(name):
                continue

            for index in range(len(name)):
                if not lower_name[index] == word[index]:
                    letter_diff += 1

            if letter_diff == 1:
                output_words.append(word)

        if len(output_words) == 0:
            print("WARNING: No similar words were found!!!")

        sorted_output_words = sorted(output_words)
        for output_word in sorted_output_words:
            print(output_word)
        print("")


if __name__ == "__main__":
    main()
