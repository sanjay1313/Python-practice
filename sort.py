def sort_your_string(string):
    string = string.split(',')
    string.sort()
    words = ""
    for value in string:
        words += value + ','     
    return words

string = input("Enter string separated by comma : ")
print("Sorted string : ",sort_your_string(string))

