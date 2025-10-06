import validators
e_mail = input("What's your email address?")
if validators.email(e_mail):
    print("Valid")
else:
    print("Invalid")
