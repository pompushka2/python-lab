password=input("Enter your password: ")
if len(password)<16:
    print("Your password is too short")
elif password.isdigit( ) or password.isalpha():
    print("Your password is to easy")
else:
    print("Your password is good")

