def palindrome(str1):
     if str1 == str1[::-1]:
         print("String is palidrome")
     else: print("Not Palindrome")
    

str1 = input("Enter string :: ")  
palindrome(str1)
    