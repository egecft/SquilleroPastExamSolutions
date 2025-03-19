INPUT_FILE_NAME = "seq.txt"
# INPUT_FILE_NAME = "seq_long.txt"


def file_reader():
    seq_list = list()
    try:
        with open(INPUT_FILE_NAME, "r") as input_file:
            for line in input_file:
                seq = list()
                clean_line = line.strip()
                clean_line_list = clean_line.split(" ")
                for num in clean_line_list:
                    seq.append(int(num))
                seq_list.append(seq)
            return seq_list
    except OSError:
        exit("Error")


def munodi_test():
    seq_list = file_reader()
    value_list = list()
    lenght_list = list()
    for sequence in seq_list:
        value_test = True
        if len(sequence) == 1:
            value_list.append(value_test)
            lenght_list.append(len(sequence))
            continue

        for index in range(len(sequence)):
            if sequence[index] == 1:
                value_list.append(value_test)
                lenght_list.append(len(sequence))
                break
            else:
                if sequence[index] % 2 == 0:
                    if sequence[index]/2 != sequence[index + 1]:
                        value_test = False
                        value_list.append(value_test)
                        lenght_list.append(len(sequence))
                        break
                else:
                    if sequence[index] * 3 + 1 != sequence[index + 1]:
                        value_test = False
                        value_list.append(value_test)
                        lenght_list.append(len(sequence))
                        break
    return value_list, lenght_list


def main():
    value_list = munodi_test()[0]
    lenght_list = munodi_test()[1]
    for index, value in enumerate(value_list):
        if value:
            print(f"Sequence {index + 1} is a Munodi sequence (Length {lenght_list[index]})")
        else:
            print(f"Sequence {index + 1} is NOT a Munodi sequence (Length {lenght_list[index]})")


if __name__ == "__main__":
    main()
