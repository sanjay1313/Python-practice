import re

def validation(password):
    flag = 0
    while True:
        if len(password) < 6 or len(password) >12:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[$#@]", password):
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            break
    if flag == 0: 
        return password
        
passwords = input("Enter Passwords :: ")
valid_pass = []
pass_list = passwords.split(',')
for value in pass_list:
    x = validation(value)
    if x is None:
        pass
    else:
        valid_pass.append(x)
print(valid_pass)
