import sys

points = 0      
while True and points < 12 :
    speed = int(input("Enter Speed :: "))
    if speed <= 70 and points < 12:
        print("oK")
    elif speed >= 71 and speed <= 129 and points < 12:
        num = int((speed - 70)//5)
        points += num
        print("Your current points : ",points)
    else:
        print("Your License expired ")
        sys.exit()
print("Your License expired ")
