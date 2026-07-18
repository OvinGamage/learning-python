shopping_cart=[]
no_items=0
total_price=0
for  no_items in range(0,11):
     item=input("add something to your shopping cart:")
     shopping_cart.insert(0,item)
     print(f"{item} is added to your shopping cart")
     price=float(input(f"enter the price of {item}:"))
     total_price+=price
     no_items+=1
     y=input("Will that be all(y/n)")
     if y=="y":
         print("thank you for shopping")
         break
if no_items==10:
    print("you have purchased the maximum amount of items")
print("-----YOUR CART-----")
for item in shopping_cart:
    print(item)
print(f"Total price:${total_price}")
