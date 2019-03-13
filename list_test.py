def separate(gadgets):
    print("String list :",str1_list)
    print("Numeric List : ",num_list)

def string_asc(gadgets):
    str1_list.sort()
    print("String list in Asc order : ",gadgets)
    
def string_desc(gadgets):
    str1_list.sort(reverse = True)
    print("String list in desc order : ",str1_list)

def num_asc(gadgets):
    num_list.sort()
    print("Numeric data from Lowest to highest : ",num_list)

def num_desc(gadgets):
    num_list.sort(reverse = True)
    print("Numeric data from Highest to Lowest : ",num_list)
        

gadgets = ["Python", "Java", 100, "Php", 310.28, "C#", 27.00,"Asp", 1000, "R", "Django"]
print("User List :: ", gadgets)
str1_list = []           
num_list = []
for value in gadgets:
    if type(value) == str:
        str1_list.append(value)
    else: num_list.append(value)  
flag = 'y'
while(flag == 'y'):
    print("\n\n")
    print("Press 'a' for Separate List")
    print("Press 'b' for string in Asc order")
    print("Press 'c' for string in Desc order")
    print("Press 'd' for Number from Lowest to Highest")
    print("Press 'e' for Number from Hihest to Lowest")
    
    choice = input("Enter your Choice : ") 
    if (choice == 'a'):
        separate(gadgets)
    elif (choice == 'b'):
        string_asc(gadgets)
    elif (choice == 'c'):
        string_desc(gadgets)
    elif (choice == 'd'):
        num_asc(gadgets)
    elif (choice == 'e'):
        num_desc(gadgets)
    else:
        print("Please!!.. enter the correct option")
    print("\n")
    flag = input("Would you like to input more(y/n) :: ")
    



        


