INPUT_FILE_GAMES = "games.csv"
# INPUT_FILE_GAMES = "games_short.csv"
INPUT_FILE_PLAYERS = "players.csv"
# INPUT_FILE_PLAYERS = "players_short.csv"


def delta(player_1, player_2):
    return 1 / (1 + 2 ** ((player_1 - player_2) / 100))


def read_games():
    games_list = list()
    try:
        with open(INPUT_FILE_GAMES, "r") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line == "PLAYER A,PLAYER B,RESULT":
                    continue
                splitted_line = clean_line.split(",")

                if splitted_line[2] == "1-0":
                    games_list.append((splitted_line[0], splitted_line[1], "w"))
                elif splitted_line[2] == "0-1":
                    games_list.append((splitted_line[0], splitted_line[1], "l"))
                elif splitted_line[2] == "1/2-1/2":
                    games_list.append((splitted_line[0], splitted_line[1], "d"))
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return games_list


def read_players():
    players_dict = dict()
    try:
        with open(INPUT_FILE_PLAYERS, "r") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line == "PLAYER,SELO":
                    continue
                splitted_line = clean_line.split(",")
                try:
                    players_dict[splitted_line[0]] = int(splitted_line[1])
                except ValueError as problem:
                    exit(f"We have a problem: {problem}")
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return players_dict


def main():
    games_list = read_games()
    players_dict = read_players()

    for player_1, player_2, game_result in games_list:
        if player_1 not in players_dict.keys():
            players_dict[player_1] = 1500
        if player_2 not in players_dict.keys():
            players_dict[player_2] = 1500

        if game_result == "w":
            players_dict[player_1] += round(200 * delta(players_dict[player_1], players_dict[player_2]))
            players_dict[player_2] -= round(200 * delta(players_dict[player_1], players_dict[player_2]))
        elif game_result == "l":
            players_dict[player_2] += round(200 * delta(players_dict[player_2], players_dict[player_1]))
            players_dict[player_1] -= round(200 * delta(players_dict[player_2], players_dict[player_1]))
        elif game_result == "d":
            pass
    for player, selo in players_dict.items():
        print(f"{player}: {selo}")


if __name__ == "__main__":
    main()
