def count_words(string):
    return len(string.split())


def count_letters(string):
    character_count = {}

    for char in string:
        char = char.lower()

        if char not in character_count:
            character_count[char] = 0

        character_count[char] += 1

    return character_count


def print_report(file_path, word_count, letter_counts):
    print("--- Begin report of {0} ---".format(file_path))
    print("{0} words found in the document\n".format(word_count))

    # sort the characters and filter out any non-alphanumerics
    new_letter_counts = {
        key: value for key, value in letter_counts.items() if key.isalpha()
    }
    new_letter_counts = dict(
        sorted(new_letter_counts.items(), key=lambda item: item[1], reverse=True)
    )

    for letter, count in new_letter_counts.items():
        print("The '{0}' character was found {1} times".format(letter, count))

    print("--- End report ---")


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as input:
        file_contents = input.read()

    # print(file_contents)

    word_count = count_words(file_contents)
    # print(word_count)

    letter_counts = count_letters(file_contents)
    # print(letter_counts)

    print_report(file_path, word_count, letter_counts)


if __name__ == "__main__":
    main()
