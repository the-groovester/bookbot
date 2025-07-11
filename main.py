def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content
    
def main(path):
    print(get_book_text(path))

main("books/frankenstein.txt")