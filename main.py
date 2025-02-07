def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        

        word_count = countWords(file_contents)
        character_counts = countChars(file_contents)
        print(len(word_count))
        print(character_counts)
        


def countWords(file):
    return file.split()

def countChars(file):
    list_of_chars = list(file)
    char_dict = {}

    for i in list_of_chars:
        lower_char = i.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict
    
    



main()

