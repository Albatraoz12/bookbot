def main(path):
    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()

        # count how many total numbers there are in the file
        remove_white_space = file_contents.split()
        total_num = len(remove_white_space)

        #count show many times a letters there are in the text ex: {'p': 6121}

        words_dict = {}

        for word in remove_white_space:
            for char in word:
                if char.isalpha():
                    char = char.lower()
                    if char in words_dict:
                        words_dict[char] += 1
                    else:
                        words_dict[char] = 1
        
        #print how many times the letter was founded
        print(f"--- Begin report of {path} ---")
        print(f"{total_num} words found in the document \n")
        
        for word in words_dict:
            print(f"The '{word}' character was found {words_dict[word]} times")

        print("--- End report ---")

path = "books/frankenstein.txt"
main(path)
