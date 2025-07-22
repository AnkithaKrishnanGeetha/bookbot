import string
import stats
import sys

#new_text = ""
""" for char in file_text:
    if(char.isalpha()):
        new_text = new_text + char
    elif(not char.isalpha()):
        new_text = new_text + " " """
    
"""for char in string.punctuation:
    file_text = file_text.replace(char," ")"""
    
    
#return len(new_text.split(" "))

def main():

    if(len(sys.argv) < 2):
        #print("Usage: python3 main.py <Path_to_book>")
        #sys.exit("Usage: python3 main.py <Path_to_book>")
        sys.stderr.write("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        #path_file = "/Users/unki/bookbot/books/frankenstein.txt"
    path_file = sys.argv[1]
    #print(get_book_text(path_file).split())
    num_words = len(stats.get_num_words(path_file))
    #print(f"{num_words} words found in the document")

    char_disctionary = stats.char_count(path_file)
    #print(char_disctionary)
    sorted_alpha_char_dict = stats.get_only_apha_char_dict(char_disctionary)
    stats.Print_report(path_file,sorted_alpha_char_dict,num_words)
main()


