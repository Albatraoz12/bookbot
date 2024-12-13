def main():
    with open('books/frankenstein.txt', "r", encoding="utf-8") as f:
        file_contents = f.read()

        # count how many total numbers there are in the file
        remove_white_space = file_contents.split()
        total_num = len(remove_white_space)
        print(total_num)

       
main()
