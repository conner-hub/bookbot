from stats import wordcounter
from stats import charactercounter
from stats import charactercount_to_list
from stats import sort_index
import sys

# Define core functions.
def get_book_text(txt):
    with open(txt) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        booktext = get_book_text(book_path)
        wordcount = wordcounter(booktext)
        charactercount = charactercounter(booktext)
        char_list = charactercount_to_list(charactercount)
        char_list.sort(reverse=True, key=sort_index)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for char_data in char_list:
            if char_data["char"].isalpha():
                print(f"{char_data["char"]}: {char_data["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()