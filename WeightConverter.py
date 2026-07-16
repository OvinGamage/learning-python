weight=int(input("Enter your weight:"))
unit=(input("Enter your unit,Kgs or Lbs"))
if unit == "Kgs":
    weight=weight*2.205
    unit="Lbs"
    print(f"your weight is{weight} {unit}")
elif unit == "Lbs":
     weight=weight/2.205
     unit="Kgs"
     print(f"your weight is{weight} {unit}")
else:
    print("Invalid unit")
