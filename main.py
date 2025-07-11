from stats import get_word_count
from stats import get_characters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content


def main(path):
    num_words = get_word_count(get_book_text(path))
    sorted_dictionary_list = sort_dictionary(get_characters(get_book_text(path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
 
    for i in sorted_dictionary_list:
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")

main("books/frankenstein.txt")