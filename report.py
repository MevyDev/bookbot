def print_letter_counts(letter_counts):
    for letter_dict in letter_counts:
        letter = letter_dict["char"]
        count = letter_dict["num"]
        print(f"{letter}: {count}")


def report(book_name, book_text, word_count, letter_map, letter_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_name}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_letter_counts(letter_counts)
    print("============= END ===============")
