from stats import get_book_word_count
from stats import char_count
from stats import sorted_chars
import sys

def get_book_text(filepath):
    with open(filepath) as text_file:
        file_contents = text_file.read() 
    return file_contents
            
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    num_words = get_book_word_count(book)
    char_num = char_count(book)
    sorted_char_count = sorted_chars(char_num)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['count']}")
    print("============ END ================")

                  


main()

