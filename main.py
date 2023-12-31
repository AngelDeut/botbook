def main():
    path = 'books/book.txt'
    print('--- Begin report of books/book.txt ---')
    text = open_file(path)

    count(text)
    
    my_dict = count_chars(text)

    sorted_chars(my_dict)




#print(file_contents)

def count(words):
    count = 0
    new_list = words.split()
    for word in new_list :
       # print(word)
        count += 1
    print(f'{count} words found in the document') 
#count(file_contents)  





def count_chars(words):
    a_to_z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    chars_dict = {}
    for letter in a_to_z:
        chars_dict[letter] = 0
    #print(chars_dict)
    words = words.lower()
    for char in words:
        if  char in chars_dict:
            chars_dict[char] += 1
    return chars_dict 

#my_dict = count_chars(file_contents)
#print(my_dict)


def sorted_chars(chars_dict):
    sorted_chars_list = []
    for char in chars_dict:
        sorted_chars_list.append((char,chars_dict[char]))         
    sorted_chars_list.sort(key=lambda a: a[1], reverse= True)
    for i in range(len(sorted_chars_list)):
        print(f"The '{sorted_chars_list[i][0]}' character was found {sorted_chars_list[i][1]} times ")
    
#sorted_chars(my_dict)    
def open_file(path):
    with open(path) as f:
        return f.read()


main()