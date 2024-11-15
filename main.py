def main():

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    
    word_count = word_counter(file_contents)
    character_count = character_counts(file_contents)
    
    print_report(word_count, character_count)

    

def print_report(word_count, character_count):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        
        sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
        
        for character, count in sorted_characters:
            if character.isalpha():
                print(f"The {character} character was found {count} times")
        print("--- End report ---")



def word_counter(file_contents):

    words = file_contents.split()
    return len(words)

def character_counts(file_contents):
    case_string = f"{file_contents}"
    lowercase_string = case_string.lower()
    characters = {}
    for character in lowercase_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters









if __name__ == "__main__":
    main()
