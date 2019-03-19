def change_string(string):
    list1 = string.split(',')
    tuple1 = tuple(list1)
    print("List  : ",list1)
    print("Tuple : ",tuple1)

string = input("Enter numbers separated by comma : ")
change_string(string)