from stats import get_book_text, get_letter_map, get_word_count, get_letter_counts

BOOKS_PATH = "books/"


def print_letter_counts(letter_counts):
    for letter_dict in letter_counts:
        letter = letter_dict["char"]
        count = letter_dict["num"]
        print(f"{letter}: {count}")


def report(book_name, books_path):
    book_text = get_book_text(book_name, books_path)
    word_count = get_word_count(book_text)
    letter_map = get_letter_map(book_text)
    letter_counts = get_letter_counts(letter_map)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_name}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_letter_counts(letter_counts)
    print("============= END ===============")


def main():
    report("frankenstein", BOOKS_PATH)


if __name__ == "__main__":
    main()
