from stats import get_book_text, get_letter_map, get_word_count, get_letter_counts

BOOKS_PATH = "books/"


def main():
    print("Welcome to bookbot! The best book analyzer on the planet!")
    print()

    book = input("Enter the name of the book you want to analyze: ")
    book_text = get_book_text(book, BOOKS_PATH)

    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

    letter_map = get_letter_map(book_text)
    print(letter_map)

    letter_counts = get_letter_counts(letter_map)
    print(letter_counts)


if __name__ == "__main__":
    main()
