# write a program which checks wethere a password is valid or not
# minimum  8 character
# atleast one lowecase
# atleast one upper case
# atleast one digit

password=input("enter the password")

lower=False
upper=False
digit=False
n=len(password)
for c in password:
    if c.islower():
        lower=True
    elif c.isupper():
        upper=True
    elif c.isdigit():
        digit=True

if  n>=8 and lower and upper and digit:
    print("strong password")
else:
    print("weak password")