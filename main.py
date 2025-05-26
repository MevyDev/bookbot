BOOKS_PATH = "books/"


def get_book_text(book_name):
    with open(BOOKS_PATH + book_name, "r") as f:
        content = f.read()
        return content


def main():
    print("Welcome to bookbot! The best book analyzer on the planet!")
    print()
    book = input("Enter the name of the book you want to analyze: ")
    book_text = get_book_text(book)

    print(book_text)


if __name__ == "__main__":
    main()
