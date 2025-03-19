INPUT_FILE_NAME = "seq.txt"
# INPUT_FILE_NAME = "seq-long.txt"


def read_file():
    seq_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split()
                seq_list.append(splitted_line)
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return seq_list


def get_input():
    first_input = input("Enter the first word: ")
    second_input = input("Enter the second word: ")
    return first_input, second_input


def main():
    seq_list = read_file()
    first_input, second_input = get_input()
    seq_closest_disctance = None
    current_min = 0

    for index_seq, seq in enumerate(seq_list):

        indexes_1 = list()
        for index_1, word_1 in enumerate(seq):
            if word_1 == first_input:
                indexes_1.append(index_1)

        indexes_2 = list()
        for index_2, word_2 in enumerate(seq):
            if word_2 == second_input:
                indexes_2.append(index_2)

        for index_1 in indexes_1:
            for index_2 in indexes_2:
                if seq_closest_disctance is None or abs(index_1 - index_2) < current_min:
                    seq_closest_disctance = index_seq
                    current_min = abs(index_1 - index_2)

    if seq_closest_disctance is None:
        print("The two words never appear in the same sequence")
    else:
        print(f"Min distance: sequence {seq_closest_disctance + 1} (distance = {current_min})")


if __name__ == "__main__":
    main()
