from stats import get_num_words, get_occurrences_map, get_char_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    #bookPath = "books/frankenstein.txt"
    content = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    omap = get_occurrences_map(content)
    #print(omap)

    char_counts = get_char_counts(omap)
    for entry in char_counts:
        c1 = entry["char"]
        c2 = entry["num"]
        if c1.isalpha():
            print(f"{c1}: {c2}")


main()
