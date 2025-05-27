def get_book_text(book_path):
    with open(book_path, "r") as f:
        content = f.read()
        return content


def get_word_count(text):
    words = text.split()
    return len(words)


def get_letter_map(text):
    letter_map = {}
    text = text.lower()
    for char in text:
        if char in letter_map:
            letter_map[char] += 1
        else:
            letter_map[char] = 1
    return letter_map


def get_letter_counts(letter_map):
    letter_counts = []
    for letter in letter_map:
        if not letter.isalpha():
            continue
        current_letter = {"char": letter, "num": letter_map[letter]}
        letter_counts.append(current_letter)
    letter_counts.sort(reverse=True, key=lambda dict: dict["num"])
    return letter_counts
