list1 = []
ran  = int(input("Enter range to insert data :: "))
for i in range(ran):
    x = input("Enter Number : ")
    list1.append(x)
    
list1.sort(reverse = True)
print("\n\n")
print("First Highest No : ",list1[0])
print("Second highest No: ",list1[1])
    
    

