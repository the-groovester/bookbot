def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content

def get_word_count(book_string):
    return len(book_string.split())


def main(path):
    num_words = get_word_count(get_book_text(path))

    print(f"{num_words} words found in the document")

main("books/frankenstein.txt")