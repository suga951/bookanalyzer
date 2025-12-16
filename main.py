def get_book_text(filepath):
    
    with open(filepath) as text_file:
        file_contents = text_file.read() 
    return file_contents

def get_book_word_count(book_string):
    book_words = book_string.split()
    return len(book_words)
               
def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_book_word_count(book)
    print(f"Found {num_words} total words")

                  


main()

