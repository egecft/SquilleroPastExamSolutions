ARTISTS = "artists.txt"
QUEEN = "queen.txt"
KISS = "kiss.txt"
ACDC = "acdc.txt"


def read_artists():
    artists_dict = dict()
    try:
        with open(ARTISTS, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(";")
                artists_dict[splitted_line[1]] = splitted_line[0]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return artists_dict


def read_songs(artist_1, artist_2, artist_3):
    artists_dict = read_artists()
    songs_dict = dict()
    try:
        with open(artist_1, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(";")
                if splitted_line[0] not in songs_dict.keys():
                    songs_dict[splitted_line[0]] = [(splitted_line[1], artists_dict[artist_1])]
                else:
                    songs_dict[splitted_line[0]] += [(splitted_line[1], artists_dict[artist_1])]

        with open(artist_2, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(";")
                if splitted_line[0] not in songs_dict.keys():
                    songs_dict[splitted_line[0]] = [(splitted_line[1], artists_dict[artist_2])]
                else:
                    songs_dict[splitted_line[0]] += [(splitted_line[1], artists_dict[artist_2])]

        with open(artist_3, "r") as file:
            for line in file:
                clean_line = line.strip()
                splitted_line = clean_line.split(";")
                if splitted_line[0] not in songs_dict.keys():
                    songs_dict[splitted_line[0]] = [(splitted_line[1], artists_dict[artist_3])]
                else:
                    songs_dict[splitted_line[0]] += [(splitted_line[1], artists_dict[artist_3])]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return songs_dict


def main():
    read_artists()
    song_dict = read_songs(QUEEN, KISS, ACDC)
    for year, songs in song_dict.items():
        print(f"{year}:")
        for song, artist in songs:
            print(f"{song:<30s} {artist}")


if __name__ == "__main__":
    main()
