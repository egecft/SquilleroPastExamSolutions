INPUT_FILE_NAME = "glucometers.txt"


def read_file():
    glucometer_dict = dict()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split()
                if splitted_line[0] not in glucometer_dict.keys():
                    glucometer_dict[splitted_line[0]] = [(splitted_line[1], splitted_line[2])]
                else:
                    glucometer_dict[splitted_line[0]] += [(splitted_line[1], splitted_line[2])]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return glucometer_dict


def main():
    glucometer_dict = read_file()
    for patient, value_list in glucometer_dict.items():
        for time, value in value_list:
            try:
                if int(value) >= 200:
                    print(f"{patient} {time} {value}")
            except ValueError as problem:
                exit(f"We have a problem: {problem}")
        print("")


if __name__ == "__main__":
    main()
