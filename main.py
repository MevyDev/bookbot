BOOKS_PATH = "books/"


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(book_name):
    with open(BOOKS_PATH + book_name + ".txt", "r") as f:
        content = f.read()
        return content


def main():
    print("Welcome to bookbot! The best book analyzer on the planet!")
    print()

    book = input("Enter the name of the book you want to analyze: ")
    book_text = get_book_text(book)

    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")


if __name__ == "__main__":
    main()
