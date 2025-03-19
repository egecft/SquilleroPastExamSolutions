INPUT_FILE_NAME = "scores.txt"


def file_reader():
    score_dict = dict()
    try:
        with open(INPUT_FILE_NAME, "r") as file:
            for line in file:
                clean_line = line.strip()
                clean_line_list = clean_line.split()

                full_name = clean_line_list[0] + " " + clean_line_list[1]
                sex = clean_line_list[2]
                nation = clean_line_list[3]
                scores = clean_line_list[4:]

                try:
                    scores = [float(x) for x in scores]
                    scores.sort()
                except ValueError:
                    exit("Value Error")

                final_score = sum(scores[1:4])
                score_dict[full_name] = [sex, nation, final_score]
            return score_dict
    except OSError:
        exit("File Reading Error")


def find_female_winner():
    score_dict = file_reader()
    female_winner_name = str()
    female_winner_nation = str()
    female_winner_score = 0

    for athlete in score_dict.keys():
        female_winner_name = athlete
        current_sex = score_dict[athlete][0]
        current_nation = score_dict[athlete][1]
        current_score = score_dict[athlete][2]

        if current_sex == "F" and current_score > female_winner_score:
            female_winner_score = current_score
            female_winner_name = athlete
            female_winner_nation = current_nation
    return female_winner_name, female_winner_nation, female_winner_score


def find_overall_winner():
    overall_dict = dict()
    score_dict = file_reader()

    for athlete in score_dict.keys():
        current_nation = score_dict[athlete][1]
        current_score = score_dict[athlete][2]

        if current_nation in overall_dict.keys():
            overall_dict[current_nation] += current_score
        else:
            overall_dict[current_nation] = current_score
    sorted_overall_dict = sorted(overall_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_overall_dict


def main():
    female_winner = find_female_winner()[0]
    female_winner_nation = find_female_winner()[1]
    female_winner_score = find_female_winner()[2]
    overall_winners = find_overall_winner()

    print(f"""Female Winner: 
    {female_winner}, {female_winner_nation} - Score: {female_winner_score}
    """)
    print(f"""Overall nations ranking:
    1) {overall_winners[0][0]} - Total Score: {overall_winners[0][1]}
    2) {overall_winners[1][0]} - Total Score: {overall_winners[1][1]}
    3) {overall_winners[2][0]} - Total Score: {overall_winners[2][1]}""")


if __name__ == "__main__":
    main()
