def sort_your_string(string):
    string = string.split(',')
    string.sort()
    for value in string:
       print(value,end=", ")   
    

string = input("Enter string separated by comma : ")
sort_your_string(string)

