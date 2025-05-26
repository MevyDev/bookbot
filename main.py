from stats import get_book_text, get_letter_map, get_word_count

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


if __name__ == "__main__":
    main()
