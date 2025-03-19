INPUT_FILE_NAME = "strawberry.txt"
# INPUT_FILE_NAME = "strawberry-short.txt"


def read_file():
    word_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(" ")
                for word in splitted_line:
                    if word == "":
                        continue
                    clean_word = word.strip("...").strip(",").strip(".")
                    word_list.append(clean_word)
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return word_list


def main():
    word_list = read_file()
    triplet_list = list()

    for index, word in enumerate(word_list):
        if index == (len(word_list) - 2):
            break
        if len(word_list[index]) == len(word_list[index + 1]) == len(word_list[index + 2]):
            triplet_list.append((word_list[index].upper(), word_list[index + 1].upper(), word_list[index + 2].upper()))

    for triplet in triplet_list:
        print(triplet)


if __name__ == "__main__":
    main()
