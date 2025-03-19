INPUT_FILE_SPORTIVE = "sportivi.csv"
INPUT_FILE_ZODIAC = "zodiaco.csv"


def read_sportive():
    sportive_list = list()
    try:
        with open(INPUT_FILE_SPORTIVE, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(",")

                splitted_date = splitted_line[3].split("/")
                date = splitted_date[1] + splitted_date[0]

                sportive_list.append((splitted_line[1], date))
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return sportive_list


def read_zodiac():
    zodiac_dict = dict()
    sign_dict = dict()
    try:
        with open(INPUT_FILE_ZODIAC, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(",")

                start_date = splitted_line[1].split("/")
                start_date = start_date[1] + start_date[0]
                end_date = splitted_line[2].split("/")
                end_date = end_date[1] + end_date[0]

                zodiac_dict[splitted_line[0]] = start_date, end_date
                sign_dict[splitted_line[0]] = 0
    except OSError as problem:
        exit(f"We have a problem: {problem}")

    zodiac_dict_sorted = sorted(zodiac_dict.items(), key=lambda x: x[1])
    return zodiac_dict_sorted, sign_dict


def main():
    sportive_list = read_sportive()
    zodiac_dict_sorted, sign_dict = read_zodiac()

    for goal, birth in sportive_list:
        for sign, date_tuple in zodiac_dict_sorted:
            if date_tuple[0] < birth < date_tuple[1]:
                sign_dict[sign] += int(goal)
                break

    sign_dict_sorted = sorted(sign_dict.items(), key=lambda x: x[1], reverse=True)

    for sign, total_goals in sign_dict_sorted:
        asterisks = ""
        try:
            asterisks = "*" * (int(total_goals) // 104)
        except ValueError as problem:
            exit(f"We have a problem: {problem}")
        print(f"{sign:<12}({total_goals}) {asterisks}")


if __name__ == "__main__":
    main()
