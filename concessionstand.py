menu={"pizza":3.00,
      "nachos":4.00,
      "chicken":5.00,
      "fries":3.00,
      "chips":3.00,
      "popcorn":5.50}
total=0
cart=[]

print("-------MENU-------")
for key,value in menu.items():
    print(f"{key:10}:$ {value:.2f}")
while True:
    food=input("What would you like to buy(q to quit): ").lower()
    if food == "q":
        print(f"Thank you for buying from the concession stand!You have bought{cart}")
        print(f"Your total is ${total:.2f}")

        break
    elif menu.get(food) is not None:
        cart.append(food)
        total+=menu.get(food)




