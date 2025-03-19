def one_letter_difference(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if len(word1) != len(word2):
        return False
    return sum(a != b for a, b in zip(word1, word2)) == 1


def find_similar_words(vowel_names, word_list):
    result = {}
    for name in vowel_names:
        result[name] = [word for word in word_list if one_letter_difference(name, word)]
    return result


def main():
    try:
        with open("names.txt", "r") as file:
            vowel_names = [line.strip() for line in file]
    except OSError:
        exit("There was an error with your file")

    try:
        with open("parole_italiane.txt", "r") as file:
            word_list = [line.strip() for line in file]
    except OSError:
        exit("There was an error with your file")

    print(find_similar_words(vowel_names, word_list))

    output_dict = find_similar_words(vowel_names, word_list)

    for name, output_words in output_dict.items():
        print(f"Name: {name}")

        if len(output_words) == 0:
            print("WARNING: No similar words were found!!!")

        sorted_output_words = sorted(output_words)
        for output_word in sorted_output_words:
            print(output_word)
        print("")


if __name__ == '__main__':
    main()
