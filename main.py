from stats import get_book_text, get_letter_map, get_word_count, get_letter_counts
from report import report

BOOKS_PATH = "books/"


def get_stats(book_name):
    book_text = get_book_text(book_name, BOOKS_PATH)
    word_count = get_word_count(book_text)
    letter_map = get_letter_map(book_text)
    letter_counts = get_letter_counts(letter_map)
    return book_text, word_count, letter_map, letter_counts


def main():
    book_name = "frankenstein"

    book_text, word_count, letter_map, letter_counts = get_stats(book_name)

    report(book_name, book_text, word_count, letter_map, letter_counts)


if __name__ == "__main__":
    main()
