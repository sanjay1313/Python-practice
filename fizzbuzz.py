print("\n")
def test(num):
    print("\n")
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%5 == 0:
        print("Buzz")
    elif num%3 == 0:
        print("Fizz")
    else:
        print(num)
        
num = int(input("Enter number :: "))
test(num)
        