# Program 4: Check whether age is valid and eligible for voting

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Age is valid and you are eligible for voting")
else:
    print("Age is valid but you are not eligible for voting")
