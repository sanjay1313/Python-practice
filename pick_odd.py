def pick_odd(numbers):
    str1 = ""
    num_list = numbers.split(',')
    for value in num_list:
        if int(value)%2 != 0:
            str1 += value + ','
        else: pass
    print("Odd numbers of list :: ",str1)

numbers = input("Enter list of numbers : ")
pick_odd(numbers)

