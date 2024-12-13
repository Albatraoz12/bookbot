def main():
    with open('books/frankenstein.txt', "r", encoding="utf-8") as f:
        file_contents = f.read()

        # count how many total numbers there are in the file
        remove_white_space = file_contents.split()
        total_num = len(remove_white_space)
        print(total_num)

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

        print(words_dict)
main()
