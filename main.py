from stats import count_chars, count_words

RELPATH = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_text = get_book_text(RELPATH)
    number_of_words = count_words(book_text)
    number_of_chars = count_chars(book_text)
    print(f"{number_of_words} words found in the document")
    print(f"{number_of_chars} characters found in the document")

main()
