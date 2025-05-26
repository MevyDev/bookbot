BOOKS_PATH = "books/"


def get_book_text(book_name):
    with open(BOOKS_PATH + book_name, "r") as f:
        content = f.read()
        return content


def main():
    book_name = input()
    print(get_book_text(book_name))


if __name__ == "__main__":
    main()
