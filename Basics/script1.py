print("This is a compound interest calculator")
principle=float(input("Enter the principle amount:"))
while principle <= 0:
    print("Principle cannot be less than or equal to zero ")
    principle = float(input("Enter the principle amount:"))
interest=float(input("Enter the interest rate:"))
while interest <= 0:
    print("Interest cannot be less than or equal to zero")
    interest = float(input("Enter the interest rate:"))
time=int(input("Enter the time in years:"))
while time <= 0:
    print("Time cannot be less than or equal to zero")
    time = int(input("Enter the time in years:"))
total=principle*pow(1+interest/100,time)
print(f"your total is ${total:.2f}")
