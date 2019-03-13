products = {
                "SMART WATCH": 550,
                "PHONE" : 1000,
                "PLAYSTATION": 500,
                "LAPTOP" : 1550,
                "MUSIC PLAYER" : 600,
                "TABLET" : 400
                }
products1 = {}
price = int(input("Enter Price :: "))
for i in products:
    if products[i] <= price:
        products1[i] = products[i]
        

for value in products1:
    print(value,"\t ==> ",products1[value])