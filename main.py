from stats import get_num_words, get_book_text, get_num_characters,sorter, display, main
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

main(book_path)