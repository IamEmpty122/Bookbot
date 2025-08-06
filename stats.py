def get_book_text(filepath, encoding ='utf-8'):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    with open(filepath, encoding = encoding) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(strings):
    new_word = []
    words = strings.split()
    for word in words:
        if word not in "!":
            new_word.append(word)
    number_of_words = len(new_word)
    sentence = f"Found {number_of_words} total words"
    print("----------- Word Count ----------")
    return sentence

def get_num_characters(strings):
    character_list = {}
    text = strings.lower()
    for character in text:
        if character not in character_list:
            character_list[character] = 1
        elif character in character_list:
            character_list[character] += 1
    return(character_list)

def sort_on(items):
    return items["num"]

def sorter(dictionary):

    list_of_dic = []

    for key in dictionary:
        new_dic = {
            "char" : key,
            "num": dictionary[key]
        }
        list_of_dic.append(new_dic)
    list_of_dic.sort(reverse=True, key=sort_on)
    return list_of_dic

def display(final_list):
    print("--------- Character Count -------")
    for dictionary in final_list:
        if dictionary['char'].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")

def main(book_path):
    string = get_book_text(book_path)
    print(get_num_words(string))
    s = get_num_characters(string)
    t = sorter(s)
    display(t)

