import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(path_to_book: str) -> str:
    """Read and return the contents of the book at the given path."""
    try:
        with open(path_to_book, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path_to_book}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{path_to_book}': {e}")
        sys.exit(1)

def print_report(path_to_book: str) -> None:
    """Analyze the book and print a report."""
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

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_report(sys.argv[1])

if __name__ == "__main__":
    main()