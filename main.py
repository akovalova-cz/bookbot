from stats import sort_unique_characters, get_num_words, get_book_text, get_unique_characters

import sys, os

def main():
   # book_path = "books/frankenstein.txt"
    print("============ DEBUG INFO ============")
    print(sys.argv)
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    if not (os.path.exists(book_path)):
        print(f"Book file not found at {book_path}")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    num_words = get_num_words(get_book_text(book_path))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    unique_chars = sort_unique_characters(get_unique_characters(get_book_text(book_path)))
    for item in unique_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()