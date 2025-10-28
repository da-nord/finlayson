#133


def validate_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        raise ValueError ("invalid email adress")
    
email=input("give me your email ")

try:
    validate_email(email)
    #login(email)
    print("logged in successfully ")
except ValueError as e:
    #if valueerror raised
    print(e)

print("eggs")