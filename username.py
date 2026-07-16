print("Rules for creating a username")
print("1.Username must be more than 12 characters long")
print("2.Username must not contain spaces")
print("3.Username must not contain digits")
username=(input("enter your username"))
if len(username)>12:
    print("username must be more than 12 characters long")
elif not username.find(" ")==-1:
    print("username must not contain  spaces")
elif not username.isalpha()==True:
    print("username must not contain digits")
else:
    print("Thanks for entering your username")
