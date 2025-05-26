def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(book_name, books_path):
    with open(books_path + book_name + ".txt", "r") as f:
        content = f.read()
        return content
