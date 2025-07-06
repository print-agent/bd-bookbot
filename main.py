from stats import count_chars, count_words, sort_chars
import sys

RELPATH = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def run_commands():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    book_text = get_book_text(run_commands())
    number_of_words = count_words(book_text)
    number_of_chars = count_chars(book_text)
    sorted_dictionaries = sort_chars(number_of_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for sort_item in sorted_dictionaries:
        print(f"{sort_item['char']}: {sort_item['num']}")

    print("============= END ===============")

main()
