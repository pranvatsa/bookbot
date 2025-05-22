import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(path_to_book):
    file_contents = ""
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()