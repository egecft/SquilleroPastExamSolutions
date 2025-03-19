INPUT_FILE_NAME = "bowling.txt"


def bowling():
    bowling_dict = dict()
    ten_dict = dict()
    zero_dict = dict()
    try:
        with open(INPUT_FILE_NAME, "r") as input_file:
            for line in input_file:
                clean_line = line.strip()
                splitted_line = clean_line.split(";")
                name_surname = splitted_line[0] + " " + splitted_line[1]
                score_list = splitted_line[2:]

                if "10" in score_list:
                    ten_dict[name_surname] = score_list.count("10")

                elif "0" in score_list:
                    zero_dict[name_surname] = score_list.count("0")

                total_score = 0
                try:
                    for score in score_list:
                        total_score += int(score)
                except ValueError as problem:
                    exit(f"We have a problem: {problem}")
                bowling_dict[name_surname] = total_score
    except OSError as problem:
        exit(f"We have a problem: {problem}")

    sorted_score_dict = sorted(bowling_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_ten_dict = sorted(ten_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_zero_dict = sorted(zero_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_score_dict, sorted_ten_dict, sorted_zero_dict


def main():
    sorted_score_dict, sorted_ten_dict, sorted_zero_dict = bowling()

    for name, score in sorted_score_dict:
        print(f"{name} {score}")
    print(f"{sorted_ten_dict[0][0]} has knocked down all the pins {sorted_ten_dict[0][1]} times")
    print(f"{sorted_zero_dict[0][0]} has missed all the pins {sorted_zero_dict[0][1]} times")


if __name__ == "__main__":
    main()
