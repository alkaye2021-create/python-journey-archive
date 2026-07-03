correct_password = "bob"
password = ""
attempts = 0

while password != correct_password and attempts < 3:
    password = input("What is the password? ")
    attempts = attempts + 1

if password == correct_password:
    print("access granted")
else:
    print("access denied")

if password == correct_password:
    print("access granted")
else:
    print("access denied")