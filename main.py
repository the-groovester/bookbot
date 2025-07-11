from stats import get_word_count
from stats import get_characters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content


def main(path):
    num_words = get_word_count(get_book_text(path))

    print(f"{num_words} words found in the document")
    print(get_characters(get_book_text(path)))

    print(sort_dictionary(get_characters(get_book_text(path))))
main("books/frankenstein.txt")