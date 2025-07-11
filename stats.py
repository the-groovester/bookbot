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

def return_char_count(items):
    return items["count"]

def sort_dictionary(char_dictionary):
    #the function takes a dictionary and appends it to a 2 key/value pair dictionary
    #is discards non-letters with .isalpha() and appends to a list
    #the list of dictionaries is sorted with .sort() and calling the return_char_count function
    list_char_count = []
    for key in char_dictionary.keys():
        dict_char_count = {}
        if key.isalpha():
            dict_char_count.update({"char": key, "count": char_dictionary[key]})
            list_char_count.append(dict_char_count)

    list_char_count.sort(reverse=True, key=return_char_count)
    return list_char_count
