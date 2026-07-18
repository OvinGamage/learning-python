rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))
symbol=input("enter the symbol:")
for x in range(rows):
    for y in range(0,cols):
        print(symbol,end="")
    print()
