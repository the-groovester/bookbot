from stats import get_word_count
from stats import get_characters
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        num_words = get_word_count(get_book_text(sys.argv[1]))
        sorted_dictionary_list = sort_dictionary(get_characters(get_book_text(sys.argv[1])))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
    
        for i in sorted_dictionary_list:
            print(f"{i["char"]}: {i["count"]}")
        print("============= END ===============")
        sys.exit(0)

main()
