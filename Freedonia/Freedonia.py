INPUT_FILE_DATES = "dates.dat.txt"
# INPUT_FILE_DATES = "dates-example1.dat.txt"
# INPUT_FILE_DATES = "dates-example2.dat.txt"
INPUT_FILE_RULES = "rules.dat.txt"
# INPUT_FILE_RULES = "rules-example1.dat.txt"
# INPUT_FILE_RULES = "rules-example2.dat.txt"


def read_rules():
    rules_dict = dict()
    try:
        with open(INPUT_FILE_RULES, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split()

                splitted_date = splitted_line[0].strip(":").split("-")
                reverse_date = splitted_date[2], splitted_date[1], splitted_date[0]

                rules_dict[reverse_date] = splitted_line[1:]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return rules_dict


def read_dates():
    dates_list = list()
    try:
        with open(INPUT_FILE_DATES, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_dates = clean_line.split("-")
                dates_list.append((splitted_dates[2], splitted_dates[1], splitted_dates[0]))
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return dates_list


def main():
    rules_dict = read_rules()
    dates_list = read_dates()

    for date in dates_list:
        rule_set = set()
        for rule_date, rule_list in rules_dict.items():

            if not int(rule_date[0]) <= int(date[0]):
                break
            if int(rule_date[0]) == int(date[0]):
                if not int(rule_date[1]) <= int(date[1]):
                    break
                if int(rule_date[1]) == int(date[1]):
                    if int(rule_date[1]) == int(date[1]):
                        if not int(rule_date[2]) <= int(date[2]):
                            break

            for rule in rule_list:
                real_rule = rule.strip("+").strip("-")
                if rule[0] == "+":
                    rule_set.add(real_rule)
                elif rule[0] == "-":
                    rule_set.remove(real_rule)

        print(f"{date[2]}-{date[1]}-{date[0]}:")
        for rule in sorted(rule_set):
            print(f"- {rule}")
        print("")


if __name__ == "__main__":
    main()
