import sys
from stats import get_book_text, get_letter_map, get_word_count, get_letter_counts
from report import report


def get_stats(book_path):
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    letter_map = get_letter_map(book_text)
    letter_counts = get_letter_counts(letter_map)
    return book_text, word_count, letter_map, letter_counts


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_name = book_path.split("/")[-1].split(".")[0]

    _, word_count, _, letter_counts = get_stats(book_path)

    report(book_name, word_count, letter_counts)


if __name__ == "__main__":
    main()
