with open('book.txt') as f:
    file_contents = f.read()

#print(file_contents)

def count(words):
    count = 0
    new_list = words.split()
    for word in new_list :
        print(word)
        count += 1
    print(count) 
count(file_contents)       


