def count_letters_digits(sentence):
    letter = digit = 0
    for value in sentence:
        if value.isalpha():
            letter += 1
        elif value.isdigit():
            digit += 1
        else: pass
    print("Letters : ",letter)
    print("Digits  : ",digit)
    
sentence = input("Enter sentence :: ")
count_letters_digits(sentence)

