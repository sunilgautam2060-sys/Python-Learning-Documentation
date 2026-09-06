

password=input("enter the password ")
email=input("enter the email ")


if password=="":
    print("password can not be empty")
    bool=False

else:

    if len(password)<8:
        print("password must be 8 character long")
        bool=False

    if password.lower()==password:
        print("password must include atleast 1 uppercase")
        bool=False

    if password.upper()==password:
        print("password must include atleast 1 lowercase")
        bool=False

    if password==email:
        print("password can not be same as the email")
        bool=False

    if " " in password:
        print("password can not contain any spaces")
        bool=False

    if not password[0].isalnum() or not password[-1].isalnum():
        print("password must start and end with a letter or digit")
        bool=False


if bool==True:
    print("password is valid")