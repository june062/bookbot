def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        

        word_count = countWords(file_contents)
        character_counts = countChars(file_contents)
        createReport(word_count,character_counts)
        


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
def createReport(word_count, char_counts):
    print(f"{len(word_count)} words were found")

    for char_count in char_counts:
        if char_count.isalpha() == True:
            print(f"'{char_count}' was found {char_counts[char_count]} times")
    
    



main()

