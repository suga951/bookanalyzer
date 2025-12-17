def get_book_word_count(book_string):
    book_words = book_string.split()
    return len(book_words)
               
def char_count(book_string):
    lower_case_string = book_string.lower()
    chars = {}
    
    for char in lower_case_string:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1    
    return chars

def sort_key(d):
    return d["count"]
def sorted_chars(char_dict):

    sorted_chars = []

    for char, count in char_dict.items():
        sorted_chars.append({'char':char,'count':count})

    sorted_chars.sort(reverse=True,key=sort_key)
    
    return sorted_chars
