from stats import count_chars, count_words, sort_chars

RELPATH = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_text = get_book_text(RELPATH)
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
