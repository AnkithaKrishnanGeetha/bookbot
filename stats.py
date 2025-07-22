import string

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text

def get_num_words(filepath):
    return get_book_text(filepath).split()

def char_count(filepath):
    file_text = get_book_text(filepath)
    char_dict = {}
    for letter in file_text:
        lowered = letter.lower()
        if(lowered in char_dict):
            char_dict[lowered] += 1 
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_by_count(char_dict):
    return char_dict["Count"]

def get_sorted_dictionary(chardict):
    charlist = []
    for char in chardict:
       charlist.append({"char" : char, "Count" : chardict[char]})
    
    charlist.sort(reverse = True, key = sort_by_count)
    return charlist

def get_only_apha_char_dict(char_dict):
    sorted_dict = {}
    charlist = get_sorted_dictionary(char_dict)
    for item in charlist:
        if(item["char"].isalpha()):
            sorted_dict[item["char"]] = item["Count"]
    return sorted_dict

def Print_report(path_file,sorted_alpha_char_dict,num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char,Count in sorted_alpha_char_dict.items():
        print(f"{char}: {Count}")
        
    print("============= END ===============")

