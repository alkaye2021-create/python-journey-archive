age = int(input("how old are you? "))
day = input("what day is it? ").lower()
has_voucher = input("do you have a voucher? yes/no ").lower()

has_voucher = input("do you have a voucher? yes/no").lower()
wants_photo_pass = input("do you want a photo pass? yes/no ").lower()

if age < 4:
    price = 0
    print("babies discount")
elif age < 18:
    price = 5
    print("child entry")
elif age >= 65:
    price = 6
    print("OAP discount!")
else:
    price = 10
    print("standard adult entry")

if day == "saturday" or day == "sunday":
    price += 2
    print("weekend surcharge added")

if has_voucher == "yes":
    price -= 3
    print("voucher discount applied")

if wants_photo_pass == "yes":
    price += 4
    print("photo pass added")

if price < 0:
    price = 0

print(f"you must pay ${price} to enter")



