def get_word_count(book_string):
    return len(book_string.split())

def get_characters(book_string):
    #function takes a string and lowers it
    #the function then initiates a dictionary and iterates over the lowered string
    #if the character is not in the list of key-values, it updates the dictionary with the key
    #if the key is in the dictionary, it adds 1 to the value
    char_dict = {}
    for char in book_string.lower():
        if char not in char_dict.keys():
            char_dict.update({char:1})
        elif char in char_dict.keys():
            char_dict[char] += 1

    return char_dict